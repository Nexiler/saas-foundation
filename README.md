# Frontend assets

This project uses `django-tailwind`, Tailwind CSS 3, and Flowbite 2. The browser receives one local, minified stylesheet; it does not download or compile Tailwind at runtime.

Tailwind scans every Django template under `src/**/templates/**/*.html`, keeps the classes that are actually used, and removes the rest. Flowbite's styles are part of the same build. Its interactive JavaScript is served locally from `static/vendors/flowbite.min.js`.

## Normal workflow: add a Flowbite block

1. Copy a Flowbite block from its documentation into a Django template.
2. Adjust its complete Tailwind classes as needed, for example `bg-blue-600`, `rounded-lg`, or `md:grid-cols-2`.
3. Build the stylesheet using one of the options below.
4. Refresh the page.

## Build once after making changes

If the Tailwind watcher is not running, compile the stylesheet once:

```bash
python src/manage.py tailwind build
```

Use this after adding or changing Flowbite blocks, Tailwind utility classes, or custom CSS. Then refresh the browser.

## Watch while developing

For automatic rebuilding, use two terminals:

```bash
# Terminal 1: Django
python src/manage.py runserver
```

```bash
# Terminal 2: Tailwind watcher
python src/manage.py tailwind start
```

When you save a template or the custom stylesheet, the watcher recompiles the CSS. `runserver` by itself serves the current CSS file but does not rebuild it.

## Custom styling

Prefer Flowbite blocks and Tailwind utilities first. For reusable custom CSS, add it to:

[`src/theme/static_src/src/styles.css`](src/theme/static_src/src/styles.css)

Then run `python src/manage.py tailwind build`, or leave the watcher running. Small, page-specific changes can usually remain Tailwind classes directly in the template.

## Important: do not generate class names dynamically

Tailwind only generates class names it can see when it scans the source files. Use complete classes in templates:

```html
<div class="bg-blue-600 text-white">...</div>
```

Avoid constructing class names dynamically:

```html
<div class="bg-{{ color }}-600">...</div>
```

If dynamic classes are unavoidable, add every allowed class explicitly to the `safelist` in [`src/theme/static_src/tailwind.config.js`](src/theme/static_src/tailwind.config.js).

## Deployment

Nothing needs to be run manually before deployment. Docker runs the production Tailwind build automatically, then Django runs `collectstatic`. The deployed stylesheet is minimized, fingerprinted, compressed, and cacheable.
