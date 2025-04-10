### week0 - Sales Data Analyzer

This is a simple Python script that reads sales data from a `.csv` file, processes it, and calculates the **average number of sales per customer**. The dataset does not contain a unique customer ID, so we're identifying each customer using a **combination of their name and postal code**:

```python
key = line[4].lower() + " " + line[7]
```
---

Hey there! This was week 0 of my data engineering journey. I'm not super confident about everything I've covered so far, but I made it this far nevertheless. Building a routine, a new way of thinking, learning syntax, a new language, and everything else that comes with such a drastic change has been dealt with nicely enough, in my opinion.

So far, I've covered basic Python, basic SQL, and basic Bash. I got the respective certificates from HackerRank (everything except Bash). Not that it really counts, but it's nice to be able to quantify something like learning through these certs — very happy about that (not the certs, but the quantifying aspect of it).

In the coming weeks I plan to hit the following targets.

Python - more real-world usage (files, APIs, pandas)

SQL - intermediate/advanced querying

Linux - automation, real commands

Git - treating your stuff like legit codebases

Cloud basics - AWS CLI, S3
