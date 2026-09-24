from pathlib import Path
import pypdfium2 as pdfium
import html
import sys
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path('docs')
files=[p for p in (root/'notes').glob('*.pdf') if p.name!='Georgia_Zachou_CV.pdf']
for path in files:
    out=root/'previews'/path.stem
    out.mkdir(parents=True,exist_ok=True)
    doc=pdfium.PdfDocument(str(path))
    pages=[]
    for i in range(len(doc)):
        page=doc[i]
        bitmap=page.render(scale=1300/page.get_width())
        im=bitmap.to_pil()
        im.save(out/f'{i+1}.webp','WEBP',quality=84)
        pages.append(f'<figure><img src="{i+1}.webp" width="{im.width}" height="{im.height}" loading="lazy" alt="Document page {i+1}. For selectable text, open the original PDF."><figcaption>Page {i+1} of {len(doc)}</figcaption></figure>')
        bitmap.close();page.close()
    (out/'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Document preview</title><style>body{margin:0;padding:12px;background:#25303c;font:12px/1.5 Arial,sans-serif;color:#dce5eb}figure{margin:0 auto 16px;max-width:1000px}img{display:block;width:100%;height:auto;background:white}figcaption{text-align:center;padding:8px}a{color:#a5e8dc}header{text-align:center;margin-bottom:12px}</style></head><body><header>Scroll through all pages · <a target="_blank" rel="noopener" href="../../notes/'+html.escape(path.name)+'">Open original PDF for selectable text and zoom ↗</a></header>'+''.join(pages)+'</body></html>',encoding='utf-8')
    print(path.name,len(doc),flush=True)
page=(root/'index.html').read_text(encoding='utf-8')
for path in files:
    page=page.replace('data-src="notes/'+path.name+'#view=FitH"','data-src="previews/'+path.stem+'/index.html"')
page=page.replace('PDF reader · scroll to explore','Document preview · scroll to explore')
(root/'index.html').write_text(page,encoding='utf-8')

