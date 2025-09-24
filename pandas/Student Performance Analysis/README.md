# Student Performance Analysis

An analysis of student scores and attendance using Python, Pandas, and Matplotlib.

## Project Overview

This project takes a dataset of student information, including scores in Math, Science, and English, as well as attendance records. It performs a comprehensive analysis to identify performance patterns, rank students, and visualize key metrics.

### Dataset

The dataset used is `students.csv`, which contains the following columns:
* `StudentID`: A unique identifier for each student.
* `Name`: The name of the student.
* `Math`: Score in the Math subject.
* `Science`: Score in the Science subject.
* `English`: Score in the English subject.
* `Attendance`: The student's attendance percentage.

### Analysis Covered

1.  **Data Wrangling:** Calculated `Total` and `Average` scores.
2.  **Grading System:** Assigned a letter grade (A, B, C, Fail) based on the average score.
3.  **Performance Ranking:** Identified the top 5 and bottom 5 students.
4.  **Correlation Analysis:** Examined the correlation between scores in different subjects.
5.  **Strength & Weakness Identification:** Programmatically determined the strongest and weakest subject for each student.

### Visualizations

* **Top 5 Performers (Bar Chart):** A chart showing the total scores of the highest-ranking students.
* **Attendance vs. Average Score (Scatter Plot):** A plot to explore the relationship between a student's attendance and their academic average.

### Requirements

To run this analysis, you will need Python and the following libraries:
* `pandas`
* `numpy`
* `matplotlib`

### How to Run

1.  Clone this repository to your local machine.
2.  Ensure you have Jupyter Notebook or JupyterLab installed.
3.  Place the `students.csv` file in the same directory as the notebook.
4.  Open and run the `Student Performance Analysis.ipynb` notebook.