<!-- HEADER SECTION -->

<div class='header'> 
<!-- Your header image here -->
<div class='headingImage' id='mainHeaderImage' align="center">
    <img src="https://d25yuvogekh0nj.cloudfront.net/2019/08/Twitter-Banner-Size-Guide-blog-banner-1250x500.png" width='1200' height='auto' ></img>
</div>

<!-- Put your badges here, either for fun or for information -->
<div align="center">
    <!-- Project Type -->
    <img src="https://img.shields.io/badge/Project Type-Machine Learning-purple?style=flat-square">
    <!-- Maintained? -->
    <img src="https://img.shields.io/badge/Maintained%3F-IN PROG-blue?style=flat-square"></img>
    <!-- License? (MIT is Standard, make sure you license your project via github) -->
    <img src="https://img.shields.io/github/license/boogiedev/automotive-eda?style=flat-square">
    <!-- Commit Activity? (Fill in the blanks) -->
    <img src="https://img.shields.io/github/commit-activity/m/your_username/your_repo_name?style=flat-square">
</div>

</br>

<!-- Brief Indented Explaination, you can choose what type you want -->
<!-- Type 1 -->
>Compare the average ratings in Beauty and Book category.



<!-- TABLE OF CONTENTS SECTION -->
<!-- 
In page linkings are kind of weird and follow a specific format, it can be done in both markdown or HTML but I am sticking to markdown for this one as it is more readable. 

Example:
- [Title of Section](#title-of-section)
  - [Title of Nested Section](#title-of-nested-section)

## Title of Section

### Title of Nested Section

When linking section titles with spaces in between, you must use a '-' (dash) to indicate a space, and the reference link in parentheses must be lowercase. Formatting the actual title itself has to be in markdown as well. I suggest using two hashtags '##' to emphasize it is a section, leaving the largest heading (single #) for the project title. With nested titles, just keep going down in heading size (###, ####, ...)
-->

## Table of Contents

<!-- Overview Section -->

- [Overview](#overview)
  - [Background & Motivation](#context)
  - [Hypothesis](#context)

<!-- Section 1 -->
- [Data PREP](#data)

<!-- Section 2 -->
- [Data Analysis](#feature-engineering)

<!-- Section 3 -->
- [Hypothesis Testing](#visualizations)

<!-- Contributors -->
- [Final thoughts](#contributors)

<!-- Credits -->
- [Future Steps](#credits)




<!-- Optional Line -->
---



## Overview

### Background & Motivation

Without a doubt, Amazon is the most popular online store in the US. Amzon has There are almost 197 million people visit Amanzon.com very month. During February 2020, Amanzon.com hads 2.01 billion visits. These data fit with my personal feelings that most people shop on Amazon and visit Amazon website more than 10 times a month.
When shopping at Amazon, customer rating has been referred by almost all. Can the average rating be very different for different categories, say Beauty vs. Books? If so, we should expect higher ratings in which categories? Can there be wider variability in rating in category Beauty as opposed to that in Books?


Source: statista.com 

### Hypothesis
The hypothesis is that the average ratings in Books is different with Beauty, and the raings in Books is higher than Beauty.

The first reason I set this assumption is that the quality of the book is relatively easy to measure. However, There is a personal preference for the quality of the cosmetics. Secondly, Amazon was originally engaged in book selling, but it started sold Beauty goods in 2007. Amazon will be more experienced than Beauty in product selection, storage and deliver of books. Customers will have a better buying experience and give them higher ratings

H0: The mean ratings of these two category is the same 

Ha: The mean ratings of these two category is different
<!-- SECTION 1 -->
## Data PREP


I search the data from https://nijianmo.github.io/amazon/index.html. In Beaty cotegory, there are 5,269 customer ratings and reviews from 2007 to 2018. Books dataset includes 27,164,982 reviews from 1997 to 2018. 

Raw data:

<img src='https://github.com/Nicole-LijuanChen/Patterns-in-Amazon-customer-ratings/blob/master/images/row_data.png?raw=true'></img>

Scan the data to determine what I need. Using pyspark to clean data. Make the data readable.

<img src='https://github.com/Nicole-LijuanChen/Patterns-in-Amazon-customer-ratings/blob/master/images/data_sample_view.png?raw=true'></img>



<!-- SECTION 2 -->
## Data Analysis


<img src='https://github.com/Nicole-LijuanChen/Patterns-in-Amazon-customer-ratings/blob/master/images/average_ratings_plot.png?raw=true'></img>


<!-- SECTION 3 -->
## Hypothesis Testing
HO: The mean ratings of these two category is the same 
H1: The mean ratings of these two category is different
Alpha: 0.01 
Using Welch's t-test to calculate P-value
Ttest result:
pvalue=1.9895758749664697e-152

Conclusion:
# p-value is small than alpha, there are enough advience to reject H0.
# The mean ratings of Beauty and Books are different.








<!-- Another line -->
---

## Contributors
[Teammate 1](https://github.com/atsai24)  | [Teammate2](https://github.com/boogiedev) | [Teammate 3](https://github.com/Nicole-LijuanChen)
---|---|---|
Alex Tsai  |  Wesley Nguyen  | Nicole Chen  |


## Credits
<!-- You can fill in packages, or particularly helpful modules, instructors, etc in here that you'd like to credit. -->



## License
[MIT ©](https://choosealicense.com/licenses/mit/)
