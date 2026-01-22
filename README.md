![head.png](figures/head.jpg)

# Financial Data Analytics in Python

**Jun.-Prof. Dr. Fabian Woebbeking**</br>
Assistant Professor of Financial Economics

IWH - Leibniz Institute for Economic Research</br>
MLU - Martin Luther University Halle-Wittenberg

fabian.woebbeking@iwh-halle.de

## Course Description

This course is designed to provide students with a hands-on understanding of the use of data science techniques in the field of financial economics. Students will learn how to collect, clean, and analyze financial data using Python, SQL and other tools. Topics will include financial data visualization, time series analysis and statistical modeling. Students will work on real-world projects to apply their knowledge to financial data.

## Important links

* [Course repository](https://github.com/cafawo/FinancialDataAnalytics): Everything you need can be found or is linked on this page.
* [Stud.IP page](https://studip.uni-halle.de/dispatch.php/course/details?sem_id=5a9defd4ce9b514471199574c12ee710&again=yes): The schedule and lecture rooms are listed here.
* [Support (Q&A)](https://github.com/cafawo/FinancialDataAnalytics/discussions): Essentially a dynamic FAQ section; you can post questions and see other students’ Q&A here.
* [StudySnips Leaderboard 🏆](https://studysnips.eu.pythonanywhere.com/leaderboard/?classroom=wmh): We employ a small gamification element for honor and bonus points.

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

> ** Three **optional** homework assignments are available, for example if you have missed a previous assignment. The **best seven count** toward your grade.

## Prerequisites

* Strong interest in financial economics
* Basic knowledge of programming (preferably Python) and statistics
* All the software used during this course are open-source and free, this includes:
    * Python**
      * [GitHub Codespaces](https://github.com/features/codespaces), a server based Python environment
      * [Miniforge (conda-forge)](https://conda-forge.org/download/), to run Python locally on your machine (macOS, Windows, Linux) 
      * ... or whatever works for you
    * Git: https://git-scm.com/
    * GitHub: https://skills.github.com/

> ** We will discuss how to get you going during the first lecture. If you already have a working Python setup - great - please carry on. If you're new to Python, you can start by using our Codespaces server, which is even accessible through your tablet.

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
* Bonus points: + 10%**
  * StudySnips: https://studysnips.eu.pythonanywhere.com/
  * Quality answers in GitHub discussions: https://github.com/cafawo/FinancialDataAnalytics/discussions
  * Bug bounty (pull requests): https://github.com/cafawo/FinancialDataAnalytics/pulls

> ** Please note that the overall achievable score cannot exceed 100% (1.0).


### How to submit your work

All students are required to register using the classroom link that you can find on top of this page, see "Important links". We will discuss this during the first lecture.

You can use your existing GitHub account or create a new account free of charge. Please note that you can optionally sign up for GitHub Pro, which is offered free of charge with your university email address.

All deliverables must be submitted through this system. To this end, there is one simple rule:

**stage + commit + push = submit!**

If this doesn’t make much sense to you now, don't worry. We will discuss how to use Git and GitHub extensively, and you will have tutorial sessions for additional guidance.

### Deadlines

* Homework assignments: deadlines are communicated on GitHub Classroom and under "Important link" above.
* Case studies: deadlines will be announced with the case description.

The deadlines for all deliverables are tracked through their commit timestamps, no emails necessary. We will talk more about this later.

## Use of AI

This course embraces the use of AI systems (e.g. large language models and coding assistants) as productive tools for learning, coding, and data analysis. When used responsibly, AI can substantially improve efficiency, help explore ideas, and support understanding of complex concepts.

Using AI does not replace independent thinking or responsibility for results. Blindly copying AI-generated content without verification is strongly discouraged and may lead to incorrect or misleading outcomes.

Best practices, efficient workflows, and common pitfalls of AI-assisted coding and analysis will be discussed throughout the course.

## Structure

### Part 1: Introduction ([slides_pt1.ipynb](https://github.com/cafawo/FinancialDataAnalytics/blob/master/slides.ipynb))

* Discussion of grading scheme and deliverables
* Setting up the tech
  * Git and GitHub
  * Necessary Python libraries
* Coding with AI (best practices and prompt engineering)
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
