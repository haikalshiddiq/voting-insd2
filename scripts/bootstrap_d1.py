import json, os, pathlib, urllib.request, urllib.error
account=os.environ['CLOUDFLARE_ACCOUNT_ID']; token=os.environ['CLOUDFLARE_API_TOKEN']
base=f'https://api.cloudflare.com/client/v4/accounts/{account}/d1/database'
headers={'Authorization':f'Bearer {token}','Content-Type':'application/json'}
def call(url,method='GET',data=None):
    req=urllib.request.Request(url,method=method,headers=headers,data=json.dumps(data).encode() if data else None)
    with urllib.request.urlopen(req,timeout=30) as r:return json.load(r)
x=call(base+'?name=voting-insd2')
items=x.get('result') or []
db=next((i for i in items if i.get('name')=='voting-insd2'),None)
if not db:
    x=call(base,'POST',{'name':'voting-insd2'})
    if not x.get('success'): raise SystemExit(x)
    db=x['result']
dbid=db.get('uuid') or db.get('id')
if not dbid: raise SystemExit('D1 database ID not returned')
p=pathlib.Path('wrangler.jsonc'); cfg=p.read_text()
cfg=cfg.replace('REPLACE_WITH_D1_DATABASE_ID',dbid)
p.write_text(cfg)
print('D1 ready:',dbid)
