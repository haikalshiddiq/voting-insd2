import pathlib,sys,re
site=sys.argv[1]
p=pathlib.Path('wrangler.jsonc');s=p.read_text()
s=re.sub(r'"TURNSTILE_SITE_KEY"\s*:\s*"[^"]*"',f'"TURNSTILE_SITE_KEY": "{site}"',s)
p.write_text(s)
