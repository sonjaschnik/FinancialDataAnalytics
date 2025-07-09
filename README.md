![head.png](figures/head.jpg)

# Financial Data Analytics in Python

**Prof. Dr. Fabian Woebbeking**</br>
Assistant Professor of Financial Economics

IWH - Leibniz Institute for Economic Research</br>
MLU - Martin Luther University Halle-Wittenberg

fabian.woebbeking@iwh-halle.de


**Birte Winter**</br>
PhD Candidate, Teaching Assistant (TA)

IWH - Leibniz Institute for Economic Research</br>

birte.winter@iwh-halle.de


## Course Description

This course is designed to provide students with a hands-on understanding of the use of data science techniques in the field of finance. Students will learn how to collect, clean, and analyze financial data using Python, SQL and other tools. Topics will include financial data visualization, time series analysis and statistical modeling. Students will work on real-world projects to apply their knowledge to financial data.

## Schedule

This course consists of both lectures and accompanying tutorial sessions. The schedule and rooms are announced on Stud.IP, see important links below.

**Lectures and tutorials start as scheduled cum tempore ($t + 15$ minutes)!**

## Important links

* [Course repository](https://github.com/cafawo/FinancialDataAnalytics)
* [Stud.IP page](https://studip.uni-halle.de/dispatch.php/course/details?sem_id=5a9defd4ce9b514471199574c12ee710&again=yes)
* [Support (Q&A)](https://github.com/cafawo/FinancialDataAnalytics/discussions)

* Homework and case submission:
  * [01_setup](https://classroom.github.com/a/xNnDzJ6-) [Due Apr 16, 2025, 08:00 UTC]
  * [02_python](https://classroom.github.com/a/8wg20wgb) [Due Apr 23, 2025, 08:00 UTC]
  * [03_montecarlo](https://classroom.github.com/a/nNUaPe5P) [Due Apr 30, 2025, 08:00 UTC]
  * [04_var](https://classroom.github.com/a/k1vW46Mf) [Due Mai 7, 2025, 08:00 UTC]
  * [05_optimization](https://classroom.github.com/a/Oj_0UndG) [Due May 21, 2025, 08:00 UTC]
  * [06_nlp](https://classroom.github.com/a/q6thu-oL) [Due Jun 4, 2025, 08:00 UTC]
  * [07_datam](https://classroom.github.com/a/7x_tBXx2) [Due Jun 18, 2025, 08:00 UTC]
  * [08_django](https://classroom.github.com/a/IQVv3Q2S) [Due Jul 30, 2025, 08:00 UTC]**
  * [09_satellites](https://classroom.github.com/a/r4akALAj) [Due Jul 30, 2025, 08:00 UTC]**
  * [10_django2](https://classroom.github.com/a/E3TRo5RB) [Due Jul 30, 2025, 08:00 UTC]**
  * [Algo trading case study](https://classroom.github.com/a/gdTY4KPC) [See due dates in case description]

> ** Three **optional** homework assignments, e.g., in case you have missed a previous assignment. The **best seven** count towards your grade.

## Prerequisites

* Strong interest and pre-knowledge in financial economics
* Basic knowledge of programming (preferably Python) and statistics
* All the software used during this course are open-source and/or free, this includes:
    * Python
      * [GitHub Codespaces](https://github.com/features/codespaces)
      * [Anaconda distribution](https://www.anaconda.com/products/distribution)
      * ... whatever works for you
    * Git: https://git-scm.com/
    * GitHub: https://skills.github.com/


## Materials

All materials are hosted as a Git repository on GitHub.

```bash
FinancialDataAnalytics/
├── cases/  # Case description and supplements
│   └── ...  
├── figures/  # Figures used in slides.ipynb
│   └── ...  
├── homework/  # Homework assignments and solutions
│   └── ...  
├── src/  # Python helper scripts (.py)
│   └── ...  
├── README.md  # Syllabus (this file)
├── slides.ipynb  # Slides
├── slides_pt[n].ipynb  # More slides, see 'structure' below
└── ...  # TBA
```

You can view or download the materials directly from GitHub, using the link above, or you can clone the repository using
```Bash
git clone https://github.com/cafawo/FinancialDataAnalytics.git
```
Make sure to update the repository regularly, especially before a lecture, using
```Bash
git pull
```

## Reading

This course is predominantly hands on and draws from several subject areas, such as financial economics, data science or textual analysis. As such, there exists no single text book recommendation. Relevant 'reading' material is linked in the script. That being said, resources include but are not limited to:
* ["Python Data Science Handbook" (Jake VanderPlas)](https://jakevdp.github.io/PythonDataScienceHandbook/)
* ["Python for Finance" (Yves Hilpisch)](https://github.com/yhilpisch/py4fi2nd)
* "Data Analysis for Business, Economics, and Policy" (Gabor Bekes, Gabor Kezdi)
* "Applied Text Analysis with Python" (Benjamin Bengfort, Rebecca Bilbro, Tony Ojeda)
* "The big short" (A. McKay)
* "Margin Call" (J. C. Chandor)
* https://stackoverflow.com/
* https://docs.python.org/3/tutorial/index.html
* https://git-scm.com/book/en/v2


## Grading Policy

The grading policy is discussed in detail during the first lecture.

* Homework assignments: 30%
* Case study: 40%
* Presentation: 30%
* Bonus points: + 15%
  * StudySnips: https://studysnips.eu.pythonanywhere.com/
  * Quality answers in GitHub discussions: https://github.com/cafawo/FinancialDataAnalytics/discussions
  * Bug bounty (pull requests): https://github.com/cafawo/FinancialDataAnalytics/pulls

### How to submit your work

All students are required to register using the classroom link that you can find on top of this page, see "Important links". 

You can use your existing GitHub account or create a new account free of charge. Please note that you can optionally sign up for GitHub Pro, which is offered free of charge with your university email address.

All deliverables must be submitted through this system. To this end, there is one simple rule:

**stage + commit + push = submit!**

If this doesn’t make much sense to you now, don't worry. We will discuss how to use Git and GitHub extensively, and you will have tutorial sessions for additional guidance.

### Deadlines

* Homework assignments, have to be submitted before the next lecture.
* Case submission deadlines will be announced with the case description.

The deadlines for all deliverables are tracked through their commit timestamps. We will talk more about this later.


## Structure

### Part 1: Introduction ([slides_pt1.ipynb](https://github.com/cafawo/FinancialDataAnalytics/blob/master/slides.ipynb))

* Discussion of grading scheme
* Setting up the tech
  * Git and GitHub
  * Necessary Python libraries (Anaconda distribution)
* Introduction to the Python programming language
* Data types and structures
* Packages and modules
* Complex data structures
* Plotting

### Part 2: Stochastic and numerical methods

* Random numbers
* Probability distributions
* Cholesky decomposition
* Numerical integration
* Numerical optimization
* Stochastic processes
* Monte Carlo simulation
* Valuation
* Risk measures

### Part 3: Financial time series
* Correlation
* Linear regression models (OLS)
* Auto regressive models (AR)
* Moving average models (MA)
* Auto regressive moving average (ARMA)
* Cointegration
* Empirical stylized facts

### Part 4: Data management
* Object-oriented programming
* Loose coupling
* Market data APIs
* Structured query language (SQL)
* More on Git (.gitignore)
* Large file storage
* Virtual environments

### Part 5: Data sourcing
* Web scraping
* Server infrastructure
* Scheduled tasks
* Logging

### Part 6: Natural language processing (NLP)
* Processing textual data
* Bag of words
* Word embedding
* Transformer architecture
* Large Language Models (LLM)
* ChatGPT API

### Guest lecture: Agentic AI ([GitHub LINK](https://github.com/dsaad68/agno-workshop))
* Introduction to agentic AI systems
* Overview of Python's Agno framework
* Single-agent and multi-agent systems
* Agent tools and memory
* Model Context Protocol (MCP)

### Case study: TBA

## Disclaimer:

This syllabus is a general plan for the course; deviations announced to the class by the instructor may be necessary.
