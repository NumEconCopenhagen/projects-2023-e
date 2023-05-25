# Model analysis project

Run the (modelproject.ipynb).

Note: We are using Jupyter Notebook from Anaconda. There might be some issues if you are using VSCODE. 

Remember to download all the packages we have imported. There is quite a few. 
Introduction

This project aims to analyze the Aggregate Demand-Aggregate Supply (AD-AS) model and extend it with a monetary policy rule, specifically the Taylor Rule. The AD-AS model is a fundamental tool in macroeconomic analysis, examining the relationship between output and inflation. By incorporating a monetary policy rule, we can investigate the effects of different monetary policy settings on the equilibrium output and inflation dynamics within the model.

Objectives

The objectives of this project are as follows:

Apply numerical model analysis methods, including optimization and equation solving techniques.
Structure the code project to ensure clarity, modularity, and organization.
Document the code thoroughly to enhance readability and understandability.
Present the results in text form and through visually appealing figures.
Model Description

The AD-AS model provides insights into the relationship between the overall level of output (Y) and the general price level (P). The model incorporates both aggregate demand (AD) and aggregate supply (AS) curves to analyze the dynamics of output and inflation in the economy. The AD curve captures the relationship between output, inflation, and other variables such as government spending and taxation. The AS curve reflects the relationship between output, inflation, and various supply-side factors.

Methodology

To solve the AD-AS model, numerical optimization and equation solving techniques are employed. The steady state equation of the model is solved to determine the equilibrium output level. The resulting equation is then converted into a function using the sympy library for numerical calculations. The AD and AS curves are defined as functions to visualize the relationship between output and inflation.

Extension: Monetary Policy Rule

In this project, we extend the baseline AD-AS model by incorporating a monetary policy rule, specifically the Taylor Rule. The monetary policy rule determines the nominal interest rate based on the inflation rate. By adjusting the inflation target and interest rate target, we can explore the impact of different monetary policy settings on the equilibrium output and inflation dynamics.

Project Structure

This project consists of the following components:

Notebook: The analysis is presented in a self-contained notebook (AD-AS_Model_Analysis.ipynb) that includes code, visualizations, and explanations.
Python Files: The Python files (my_model.py) contain the necessary functions and calculations used in the analysis.
Documentation: All code is fully documented to ensure clarity and understanding.
Results

The project provides interactive plots that visualize the AD and AS curves, allowing users to adjust shocks, inflation targets, and interest rate targets. Through these visualizations, we can observe the effects of different monetary policy settings on equilibrium output and inflation. The optimal parameter values that minimize the social loss function are also determined through numerical optimization.

Conclusion

By analyzing the AD-AS model and extending it with a monetary policy rule, this project sheds light on the dynamics of output and inflation in an economy. The project demonstrates the application of numerical model analysis methods, effective code structuring, documentation, and the presentation of results in both text and visual forms.

Future Work

Potential areas for future exploration include conducting sensitivity analyses, investigating additional extensions to the model, and incorporating more complex economic factors. These enhancements could further deepen our understanding of the AD-AS model and its implications for macroeconomic analysis.
