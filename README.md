**Numerical Labs**

A community for mathematics students and professionals to showcase their work and research in an accessible way using interactive forms and graphics.

# Introduction

Numerical Labs started during my time working on my thesis for a Master's in Mathematics at San Francisco State University. I enjoyed my research but I also enjoyed explaining my research to non math students. I wanted to come up with a way to showcase my work in a manner that was simpler and clearer to understand than a typical mathematics research paper. I also thought this could be a portal for other researchers to present their work to the public in hopes of public education and to generate interest in the sciences. So far, we have only one research topic presented (my own) but we are always on the look out for others and encouraging others to post their work to the site. Help with the formatting and graphics is always available. 

# Webapp Engineering Overview

## Core Technologies:
The webapp is built using Python and Flask, with Flask handling HTTP requests and rendering templates. For the front end, Bootstrap is used for UI design, ensuring responsiveness and consistency across different devices.

## Dynamic Content and Interactivity:
JavaScript, along with AJAX and jQuery, is used to enable dynamic content updates and interactive features without page reloads. This setup improves user interaction by providing real-time feedback and seamless content rendering.

## Data Processing and Visualization:
Backend data processing is handled using Pandas for data manipulation and SQLAlchemy for database interactions. Vega is integrated for creating interactive data visualizations, making the data more accessible and engaging for users.

## Overall Structure:
The architecture combines these technologies efficiently, ensuring a balance between dynamic front-end interactions and robust back-end data processing. The use of Jinja templates with AJAX and jQuery enhances user experience through dynamic content, while Pandas and SQLAlchemy manage the data effectively. Vega’s integration for visualization adds a layer of interactivity and insight to the user interface.


# Numerical Semigroups and the Second Frobenius Number Webpage

## Overview

This webpage, part of a larger project on numerical semigroups, provides an interactive exploration of numerical semigroup invariants and the concept of the second Frobenius number. It is designed to be a user-friendly interface for understanding and analyzing these abstract algebraic concepts, leveraging the computational power of the `semigroups.py` script.

## Key Features

1. **Interactive Exploration**: Users can interact with the webpage to input specific parameters and generate results related to numerical semigroups. The interface is designed for both educational purposes and advanced mathematical exploration.

2. **Semigroup Invariants**: The webpage focuses on key invariants of numerical semigroups, providing insights into their structure and properties. This includes calculations like the Frobenius number, gaps, and elements of the semigroup.

3. **Second Frobenius Number**: A highlight of this webpage is the exploration of the second Frobenius number, a less commonly discussed concept in numerical semigroups. This feature offers a deeper look into the more complex aspects of semigroup theory.

4. **Visualization and Data Presentation**: Utilizing the data processing and visualization capabilities of the `semigroups.py` script, the webpage presents data in a comprehensible and visually appealing manner, making the abstract concepts more accessible.

5. **Educational Tool**: The webpage serves as an excellent educational resource for students and enthusiasts of abstract algebra, particularly those interested in numerical semigroups.

## Technical Background

The webpage is built using Flask and Jinja for backend and templating, respectively. The semigroups.py script, integrated into the backend, handles the complex computational tasks, while the frontend provides a responsive and intuitive user interface using Bootstrap. JavaScript, AJAX, and jQuery are used for dynamic content rendering and handling user interactions.

## Usage

To use the webpage, simply input the desired parameters related to numerical semigroups and submit. The webpage will then display various invariants and properties, including the second Frobenius number, corresponding to the given input.


# Overview of Semigroups.py

**Purpose**: The `semigroups.py` program is designed to perform computational tasks related to the study of semigroups, a fundamental concept in abstract algebra. It focuses on generating semigroup elements, analyzing their properties, and visualizing data related to these elements.

## Key Components:

1. **SemigroupElement Class**:

* Represents an element of a semigroup.
* Stores a multiset and its cardinality.
* Provides methods to calculate the sum (`number`) and factorizations (`coefficients`) of the multiset.

2. **Semigroup Creation**:

* Function `create_semigroup` generates a semigroup from given generators and a parameter `N`.

* Utilizes combinations to create multisets and organizes them into semigroup elements.

3. **Data Analysis Functions**:

* `calc_num_of_elements_of_len_k`: Calculates the maximum factorization length and counts elements of a certain length in the semigroup.

* `calculate_invariants`: Computes invariants for the semigroup, like maximum and minimum factorization lengths, and their ratios.

* `create_invariants_for_single_element`: Similar to `calculate_invariants` but for a single specified semigroup element.

4. **Visualization and Utility Functions**:

* `create_factorization_fig`: Generates a DataFrame for visualization of length counts up to a given `N`.

* `create_example_1`: Creates a sorted list of unique numbers from the first 50 elements of the semigroup, filtered by a maximum value.

5. **Data Handling**:

* Uses `pandas` for data manipulation and possibly for visualization (though direct visualization code seems commented out).
* Incorporates `json` for data formatting or serialization.

## Application:

This program can be used to study and analyze semigroups, specifically focusing on the properties of their elements, such as sum and factorization patterns. It's particularly useful for those interested in abstract algebra and computational mathematics.



# Research Topic 1: Numerical Semigroups

A numerical semigroup is a subset of the nonnegative integers with finite complement. Every numerical semigroup contains a set of generators, that is, a minimal subset that when whose elements are added together repeatedly, create all the other elements of the semigroup. 
