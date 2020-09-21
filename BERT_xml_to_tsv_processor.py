import xml.dom.minidom
import codecs

def main():

	out= codecs.open('task1tamil.tsv','w',encoding="utf-8")

	# f=open("samplefile.txt","a", encoding="utf-8")
	doc=xml.dom.minidom.parse("task1tamil.xml")
	paraphrases=doc.getElementsByTagName("Paraphrase")
	for i in paraphrases:
		pID=i.getAttribute("pID")
		sentence1=i.getElementsByTagName("Sentence1")
		sentence2=i.getElementsByTagName("Sentence2")
		_class=i.getElementsByTagName("Class")
		out.write(pID+"\t")
		for x in _class:
		#	print x.firstChild.nodeValue
			out.write(x.firstChild.nodeValue+"\t"+"a"+"\t")

		for x in sentence1:
		#	print x.firstChild.nodeValue
			out.write(x.firstChild.nodeValue.replace("\n",""))
			#print(x.firstChild.nodeValue.replace("\n","\t").length)
		for x in sentence2:
		#	print x.firstChild.nodeValue
			out.write("<eol>"+x.firstChild.nodeValue.replace("\n","")+"\n")
		

	out.close()
if __name__=="__main__":
	main();