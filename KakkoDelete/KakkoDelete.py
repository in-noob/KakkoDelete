import re

# ファイル読み込み
inPath = "input/1.txt"
in_text_data = open(inPath,"r")
inText = in_text_data.read()
in_text_data.close()


# テキストのコンテンツ部加工処理
outputContents = inText
startList = list()
startCursor = 0
endCursor = 0
currentCursor = 0
while(1):
    startCursor = outputContents.find("{",startCursor)
    endCursor = outputContents.find("}",endCursor)
    if endCursor < 0:
        break
    
    if (startCursor < 0 and endCursor > 0) or (startCursor > endCursor):
        currentCursor = startList.pop()
        if not startList:
            outputContents = outputContents[:currentCursor]+outputContents[endCursor+1:]
            startCursor = 0
            endCursor = 0
        else:
            endCursor += 1
    elif startCursor < endCursor:
        startList.append(startCursor)
        startCursor += 1






# ファイル名加工
outputFileName = re.sub(".+\/","",in_text_data.name)
outputFileName = re.sub("\.","_",outputFileName)

# ファイル出力
outPath = "output/" + outputFileName
out_text_data = open(outPath,"w")
outText = out_text_data.write(outputContents)
out_text_data.close()
