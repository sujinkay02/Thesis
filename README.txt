{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf400
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fswiss\fcharset0 Helvetica-Bold;\f2\fswiss\fcharset0 Helvetica-Oblique;
\f3\froman\fcharset0 Times-Roman;\f4\fswiss\fcharset0 Helvetica-BoldOblique;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue233;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c93333;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Sujin Kay\
April 18, 2019\
Senior Thesis Program Instructions\
\
There are 4 separate programs that were built for the purposes of this study. All files are written in Python 3 (and thus can be run via the terminal using the command \'93python3 <filename>.py\'94.\
\
For 
\f1\b all 
\f0\b0 programs, there are clearly-labeled filepaths under the \'93MAIN\'94 section header, where relevant data files are stored locally on my computer. 
\f2\i \ul These filepaths must be renamed in correspondence to the user\'92s folders and filepaths. \

\f0\i0 \ulnone \

\f1\b Most importantly, all data files must be downloaded. This includes the Male/Female blog data, as well as the Non-Binary data. 
\f0\b0 This data is made available on Github ({\field{\*\fldinst{HYPERLINK "https://github.com/sujinkay02/Thesis"}}{\fldrslt 
\f3 \cf2 \expnd0\expndtw0\kerning0
\ul \ulc2 \outl0\strokewidth0 \strokec2 https://github.com/sujinkay02/Thesis}}
\f3 \cf2 \expnd0\expndtw0\kerning0
\ul \ulc2 \outl0\strokewidth0 \strokec2 )
\f0 \cf0 \kerning1\expnd0\expndtw0 \ulnone \outl0\strokewidth0 . Further, all 
\f2\i test files 
\f4\b must be kept in a separate folder, and the thesis_prelimdata.py and thesis_formal_v22.py files \ul must be located in the same folder as the test files\ulnone . 
\f0\i0\b0 This is because these programs must be in the same directory in order to access the pickled byte files, which are automatically stored in the same folder as the test files. 
\f1\b \
\

\f0\b0 Some tests and commands are commented out (can be uncommented depending on the user\'92s desired behavior/tests). A few commands must be 
\f2\i only 
\f0\i0 run after others; if this is the case, these instructions are explicitly defined within the program. Otherwise, no other changes to the program need to be made in order to run properly. \
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\

\f1\b thesis_data_final.py\

\f0\b0 This program was used for the following purposes:\
- Renaming the Male and Female blog files and converting from XML to text file formats\
- Scraping hyperlinks and extracting Non-Binary online article data from the Beyond the Binary website\
- Performing text pre-processing (tokenizing into words, tagging Parts of Speech)\
- Selecting and concatenating training files and test files for Male, Female, and Non-Binary files\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\

\f1\b thesis_pickling_final.py\

\f0\b0 This program was used to perform Python\'92s \'93pickling\'94 (i.e., data serialization) on the Male/Female/Non-Binary text profiles, as well as the various n-gram data structures that were produced for each gender file. \
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\

\f1\b thesis_prelimdata.py\

\f0\b0 This program was used to for the preliminary analysis and to gather the binary 
\f2\i and 
\f0\i0 non-binary gender classification accuracy results. \
It includes the following:\
- Showing frequencies of the X most common words / chars / POS tags\
- Producing n-grams-based text profiles for each test file\
- Computing dissimilarity measures using the test files and gender files \
- Computing the overall classification accuracy across n-grams sizes (n=1-5) and types (word, char, POS)\
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\

\f1\b thesis_formal_v22.py\

\f0\b0 This program was used to for the formal feature selection & extraction process, and to gather the non-binary gender classification accuracy results. \
It includes the following:\
- Same as the the prelimdata file, but using a specified feature set \
- Selects the top 3 most frequent words in each word category, to be included in the final feature set\
- Allows user to generate gender-specific classification testing / accuracies\
\
\
\
}
