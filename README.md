<h2> link_scrape.py </h2>
<br>
<p> Running this file, user is asked to input a site address, ex <a href="github.com">https://github.com</a> </p>
<br>
<p> link_scrape.py will scrape the contents of the webpage and grab all links, links are categorized is internal or external, internal links are traversed after the initial loop for additional internal/external links. The number of times an internal link and external link is present on the site is stored as well </p>
<br>
<p> After running, link_scrape.py will save a txt file containing all links and the number of times they appear in the site </p>
<br>
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
