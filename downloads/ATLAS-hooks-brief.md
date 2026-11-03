# Brief: add content hook points to the ATLAS theme

**Client:** Primion (primion.io)
**Theme:** ATLAS (custom theme, maintained by the agency)
**Date:** 3 November 2026
**Effort:** about 30 minutes plus testing
**Visible change for visitors:** none

## 1. Why

Primion will use the **ATLAS Content Blocks** plugin to place reusable content (banners, calls to action, notices) at fixed places on the site, and to show popups. The plugin works like Blocksy's Content Blocks.

The plugin places content through WordPress action hooks. Most of its locations already work with the current theme. Five do not, because the theme never fires them:

| Hook | Where it should fire | Status in the current theme |
|---|---|---|
| `wp_body_open` | Right after the opening `<body>` tag | **Missing.** This is a WordPress core hook that every theme should call since WordPress 5.2. Plugins also use it, for example for the GTM noscript tag. |
| `atlas_before_header` | Just before the site header | **Missing** |
| `atlas_after_header` | Just after the site header, before the page content | **Missing** |
| `atlas_before_footer` | After the page content, just before the site footer | **Missing** |
| `atlas_after_footer` | Just after the site footer | **Missing** |

We ask you to add these five hooks to the theme. Nothing else in the theme needs to change.

## 2. What to change

Two files in the theme root: `header.php` and `footer.php`.

**Rules:**
- Use these hook names exactly. The plugin looks for them by name.
- The calls output nothing themselves. Only code attached to the hooks outputs anything, so the page is unchanged until a content block uses them.
- Keep everything else in both files as it is, including `Theme_App::render_scripts()`, `wp_head()` and `wp_footer()`.
- Do not wrap the calls in conditions.

### 2.1 `header.php`

Current file:

```php
<?php
/**
 * The Header for theme.
 *
 * Displays all of the <head> section and page header
 *
 * @package    WordPress
 * @subpackage ATLAS
 * @since      ATLAS 1.0
 */

get_theme_part( 'html-head' );

?>
<body <?php body_class(); ?>>
<?php echo Theme_App::render_scripts( 'begin_scripts' ); ?>
<div id="page">
	<?php get_theme_part('components/header/main'); ?>
```

New file:

```php
<?php
/**
 * The Header for theme.
 *
 * Displays all of the <head> section and page header
 *
 * Hooks for placing content (used by the ATLAS Content Blocks plugin):
 * - wp_body_open        Right after <body>
 * - atlas_before_header Before the site header
 * - atlas_after_header  After the site header, before the page content
 *
 * @package    WordPress
 * @subpackage ATLAS
 * @since      ATLAS 1.0
 */

get_theme_part( 'html-head' );

?>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<?php echo Theme_App::render_scripts( 'begin_scripts' ); ?>
<div id="page">
	<?php do_action( 'atlas_before_header' ); ?>
	<?php get_theme_part('components/header/main'); ?>
	<?php do_action( 'atlas_after_header' ); ?>
```

In short:
- add `wp_body_open();` directly after `<body ...>`, before the begin scripts;
- add `do_action( 'atlas_before_header' );` directly before the header part;
- add `do_action( 'atlas_after_header' );` directly after it.

### 2.2 `footer.php`

Current file:

```php
<?php
/**
 * The footer for theme.
 *
 * @package    WordPress
 * @subpackage ATLAS
 * @since      ATLAS 1.0
 */

?>
	<?php get_theme_part('components/footer/main'); ?>
</div> <!-- /#page -->
<?php wp_footer(); ?>
<?php echo Theme_App::render_scripts( 'end_scripts' ); ?>
</body>
</html>
```

New file:

```php
<?php
/**
 * The footer for theme.
 *
 * Hooks for placing content (used by the ATLAS Content Blocks plugin):
 * - atlas_before_footer After the page content, before the site footer
 * - atlas_after_footer  After the site footer
 *
 * @package    WordPress
 * @subpackage ATLAS
 * @since      ATLAS 1.0
 */

?>
	<?php do_action( 'atlas_before_footer' ); ?>
	<?php get_theme_part('components/footer/main'); ?>
	<?php do_action( 'atlas_after_footer' ); ?>
</div> <!-- /#page -->
<?php wp_footer(); ?>
<?php echo Theme_App::render_scripts( 'end_scripts' ); ?>
</body>
</html>
```

Both new footer hooks stay **inside** `<div id="page">`, just like the header hooks.

### 2.3 Templates that bypass `header.php` or `footer.php`

Check whether any template prints its own `<body>` tag or site footer instead of calling `get_header()` and `get_footer()`. Landing page templates are the usual suspects. If you find one, add the same calls in the same positions there, or tell us which templates skip them.

## 3. How to test

Do this on staging first.

1. **Check the page is unchanged.** Compare the homepage and one post before and after the change, at 390 px and 1440 px wide. There should be no visual difference.
2. **Check each hook fires.** Add this temporary snippet as a must-use plugin, for example `wp-content/mu-plugins/atlas-hook-check.php`:

   ```php
   <?php
   // Temporary: marks where each ATLAS hook fires, for logged-in administrators only.
   foreach ( array( 'wp_body_open', 'atlas_before_header', 'atlas_after_header', 'atlas_before_footer', 'atlas_after_footer' ) as $atlas_hook ) {
   	add_action( $atlas_hook, function () use ( $atlas_hook ) {
   		if ( current_user_can( 'manage_options' ) ) {
   			echo "\n<!-- ATLAS hook: " . esc_html( $atlas_hook ) . " -->\n";
   		}
   	} );
   }
   ```

   While logged in as an administrator, view the page source of the homepage, a page, a post, an event, a webinar, a download, the search results page and the 404 page. In each one, find the five `<!-- ATLAS hook: ... -->` comments, in this order:
   1. `wp_body_open` (directly after `<body ...>`)
   2. `atlas_before_header`
   3. `atlas_after_header`
   4. `atlas_before_footer`
   5. `atlas_after_footer` (before `</div> <!-- /#page -->`)

   **Delete the snippet afterwards.**
3. **Check nothing breaks.** The browser console and the PHP error log should show no new errors. Also check:
   - The tracking scripts set in Theme Options ("Apis & Tracking") still load at the beginning and end of the body.
   - The language switcher still works on one non-English page.

## 4. Deliverables

- The updated `header.php` and `footer.php`, in the theme's version control if you use it.
- A short note confirming the test in section 3. Include the URLs you checked and any templates that do not call `get_header()` or `get_footer()`.

## 5. Rollback

Restore the two original files. Nothing else depends on the change, so rolling back is safe. While the hooks are missing, content blocks set to those five locations simply do not appear.

## 6. Out of scope

Leave all of these alone:
- Any other theme change: scripts, styles, templates, ACF fields.
- Installing or configuring the ATLAS Content Blocks plugin. Primion handles that.
- Plugin updates, server or caching changes.

## 7. Questions

Contact Primion marketing. Mention whether your theme repository already has newer versions of these files than the ones quoted above, so we can confirm the placement before you deploy.
