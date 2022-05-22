# U.S. Patent Phrase to Phrase Matching

Help Identify Similar Phrases in U.S. Patents

Source: <https://www.kaggle.com/competitions/us-patent-phrase-to-phrase-matching/overview>

Can you extract meaning from a large, text-based dataset derived from inventions? Here's your chance to do so.

The U.S. Patent and Trademark Office (USPTO) offers one of the largest repositories of scientific, technical, and commercial information in the world through its Open Data Portal. Patents are a form of intellectual property granted in exchange for the public disclosure of new and useful inventions. Because patents undergo an intensive vetting process prior to grant, and because the history of U.S. innovation spans over two centuries and 11 million patents, the U.S. patent archives stand as a rare combination of data volume, quality, and diversity.

“The USPTO serves an American innovation machine that never sleeps by granting patents, registering trademarks, and promoting intellectual property around the globe. The USPTO shares over 200 years' worth of human ingenuity with the world, from lightbulbs to quantum computers. Combined with creativity from the data science community, USPTO datasets carry unbounded potential to empower AI and ML models that will benefit the progress of science and society at large.”

— USPTO Chief Information Officer Jamie Holcombe

In this competition, you will train your models on a novel semantic similarity dataset to extract relevant information by matching key phrases in patent documents. Determining the semantic similarity between phrases is critically important during the patent search and examination process to determine if an invention has been described before. For example, if one invention claims "television set" and a prior publication describes "TV set", a model would ideally recognize these are the same and assist a patent attorney or examiner in retrieving relevant documents. This extends beyond paraphrase identification; if one invention claims a "strong material" and another uses "steel", that may also be a match. What counts as a "strong material" varies per domain (it may be steel in one domain and ripstop fabric in another, but you wouldn't want your parachute made of steel). We have included the Cooperative Patent Classification as the technical domain context as an additional feature to help you disambiguate these situations.

Can you build a model to match phrases in order to extract contextual information, thereby helping the patent community connect the dots between millions of patent documents?

```bash
kaggle competitions download -c us-patent-phrase-to-phrase-matching

kaggle competitions submit -c us-patent-phrase-to-phrase-matching -f submission.csv -m "msg"
```

```

Use the Kaggle API to download the dataset.
<https://github.com/Kaggle/kaggle-api>
