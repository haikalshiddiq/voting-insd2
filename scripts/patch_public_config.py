import pathlib,sys,re
site,email=sys.argv[1],sys.argv[2]
p=pathlib.Path('wrangler.jsonc'); s=p.read_text()
s=re.sub(r'"TURNSTILE_SITE_KEY"\s*:\s*"[^"]*"',f'"TURNSTILE_SITE_KEY": "{site}"',s)
s=re.sub(r'"ADMIN_EMAILS"\s*:\s*"[^"]*"',f'"ADMIN_EMAILS": "{email}"',s)
p.write_text(s)
