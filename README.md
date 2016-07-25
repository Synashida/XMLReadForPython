# XMLReadForPython

Namespace付きのXMLファイルを読み込むサンプル。
ファイルは総務省統計局のe-Statのhttp://e-stat.go.jp/SG2/eStatGIS/page/download.htmlより取得したGMLデータをサンプルに利用させていただいています。

```
  # Namespaceの定義を行う
  ns = {'gml': 'http://www.opengis.net/gml', 'fme': 'http://www.safe.com/gml/fme', 'xlink': 'http://www.w3.org/1999/xlink'}

  # 属性の取得
  root.find('gml:boundedBy/gml:Envelope', ns).attrib['属性名']

  # 値の取得
  itemNode.find('fme:MESH03622/fme:KEN_ID', ns).text.strip()
```

find関数で namespace配列を渡さないとノードの検索ができないため、
事前のnamespace配列が必要になります。
namespace配列は 'namesapce':'url'の形式になります。

