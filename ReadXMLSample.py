#!/usr/bin/python
# -*- coding: utf-8 -*-

# 
# 制作環境
# Python 2.7.10
#
# 制作 : 株式会社 V-FORCE 芦田 真一 
#
# NameSpaceつきのXMLをパースして値を取得する
#

from pprint import pprint
import os
import xml.etree.ElementTree as ET

if __name__ == "__main__":

  fileName = "MESH03622.gml"
  if not os.path.exists(fileName):
  	exit

  # XMLに指定されているNameSpaceをそれぞれ登録する
  # xmlns:fme="http://www.safe.com/gml/fme" これは 'fme' : 'http://www.safe.com/gml/fme' となる
  ns = {'gml': 'http://www.opengis.net/gml', 'fme': 'http://www.safe.com/gml/fme', 'xlink': 'http://www.w3.org/1999/xlink'}
  tree = ET.parse(fileName)
  root = tree.getroot()

  # AtrributeのsrsNameを取得する
  pprint ("envelope = " + root.find('gml:boundedBy/gml:Envelope', ns).attrib['srsName'].strip())

  # gml:featureMember以下を取得したい
  fmeNodes = root.findall('gml:featureMember', ns)

  records = []
  for itemNode in fmeNodes:
    # ルート以下のnodeの値が欲しい場合、rootからのパスを記述することで値が取得できる
    # findするときに namespaceの配列を指定するのを忘れずに！
    pprint ("KEN_ID = " + itemNode.find('fme:MESH03622/fme:KEN_ID', ns).text.strip())
    # 現在のitemNodeを基準に相対パス指定で取得可能
    pprint ("KEN_ID = " + itemNode.find('.//fme:KEN_ID', ns).text.strip())
    # pointlistが取得したい場合も同様でパスを記述する(長いので省略記法)
    pprint ("posList = " + itemNode.find('fme:MESH03622/gml:surfaceProperty/gml:Surface/gml:patches/gml:PolygonPatch/gml:exterior/gml:LinearRing/gml:posList', ns).text.strip())
    # データが流れ過ぎないように便宜上break
    break