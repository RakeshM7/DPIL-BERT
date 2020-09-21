Detecting Paraphrases in Indian Languages using deep learning

We have described the process of using BERT , Seq2Seq and USE algorithms to detect whether a given pair of sentence is a paraphrase or semiparaphrase or non paraphrase.

Dataset description:

We have used dataset from DPIL@FIRE2016 . The dataset contains sentence pairs in four Indian languages namely Tamil, Malayalam, Hindi and Punjabi. Task1 is to identify if the sentences are paraphrases (P) or non paraphrases (NP). Task2 is to identify if the sentences are paraphrases (P) or non paraphrases (NP) or semi paraphrases (SP).The details of this corpus can be found in http://nlp.amrita.edu/dpil_cen/ . The dataset contains both the training and testing data.

Data Preprocessing:

The training data in the data set are available in XML format.The data is present in the format - 
             SENTENCEPAIR_ID SENTENCE1 SENTENCE2 CLASS_LABEL
where the class label is P (or) NP (or) SP.

The test data is available as a xlsx file in the format
<< TODO >>

For the algorithm to operate on the date , preprocessing has to be done to convert the xml file to a tsv  and to convert it in the format as required by the algorithms. The script used for preprocessing is 
 
 1. BERT_xml_to_tsv_processor.py  for BERT 
 2. << TODO >>

Executing BERT:

1. Open BERT.ipynb file in Google colabaratory.
2. Enter the task and language name.
3. << Not required >> Specify the datapath of where the training data is. ( here the data path is hardcoded)
4. << Not required >> Specify the path of the testdata if prompted; by default, the testdata is fetched from testdata folder.
5. << Not required >> Specify where the model has to be saved; by default, the model is saved in model folder.
6. << Not required >> Specify where the results has to be saved;
7. Change the learning rate and number of epochs if you wish to.
8. Run all the blocks: Runtime -> Run all
9. The result file is saved as text file(.txt) in results folder and reults are returned in logits ( will be converted to probabilities in final execution code).



Classification:

After all the algorithms return the results , the results are fetched and processed as required for classification.
1. 
<<TODO>>
