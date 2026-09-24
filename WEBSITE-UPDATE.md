# Website update

The new site uses a custom midnight-blue design with teal accents. The biography, education, research, experience, skills, awards, and CV are updated from CV_PhD.pdf.

## Materials

Select a document in Materials to expand a scrollable reader. Each reader contains page images generated from the original PDF so it also works in browsers without a built-in PDF viewer. Original PDFs remain available through Open PDF and Download; use the original for selectable/searchable text and detailed zoom. Only one reader expands at a time, and page images load lazily.

To add a material, place its PDF under docs/notes, create its preview, and duplicate an existing details.material block in docs/index.html. Use a unique title and point the preview iframe and the open/download links to the matching files. Regenerate page previews when replacing a PDF.

The preview-generation script is provided as generate-previews.py. Run it with Python, pypdfium2 and Pillow installed, passing the docs directory as its argument.

## Backup and recovery

website-original-2026-09-22.zip contains the original docs directory, mkdocs.yml, and Readme.txt, captured before editing. Original Git HEAD: 3d26bf3f2e6386b0971af8dd514093c4562b34c5. The working tree was clean before this update.

To recover the previous site, extract the ZIP into a temporary folder and copy its docs, mkdocs.yml, and Readme.txt back into GeorgiaZ9.github.io, replacing matching files. The original index.html will use its original styles and scripts. The extra new files can remain unused. No changes to Git history are needed.

## Publishing

This update is local. It has not been committed or pushed. Review it before publishing through the repository's existing GitHub Pages process.

The active page no longer uses the old iPortfolio layout, styles, scripts, or visible credits. The old assets and their source notices are retained for recovery.
