
<h2> NER_Text.py </h2>
<br>
<p> Running this file, user is asked to input a site address, ex: <a href="github.com">https://github.com</a> </p>
<br>
<p> NER_Text.py will scrape the contents of the webpage and grab all readable text. Text is then run through a pre-trained 'Named Entity Recognition' model to isolate all named entities from the site text. </p>
<br>
<p> These entities are passed to the PyTrends API which runs a Related Queries search on the entities found by the BERT model </p>
<br>
<h3> Dependencies </h3>
<ul>
  <li> Beautiful Soup, lxml, requests </li>
  <li> pandas </li>
  <li> pytrends </li>
  <li> pytorch </li>
</ul>
