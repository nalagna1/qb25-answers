Exercise 2

Step 2.2

1. What is the “size” (i.e., slope) of this relationship?
    Interpret the slope in plain language.
      The slope is 0.3775662, suggesting that the relationship is of moderate
      strength (i.e., not strongly correlated; a slope of 1.0 would be perfect
      correlation).
      Does it match your plot?
      Yes, the scatter depicts a clear relationship between 
      the X and Y variables, but is somewhat diffuse.
      
2. Is the relationship significant?
    How do you know? Explain the p-value in plain but precise language.
      The relationship is extremely significant. The p-value is 6.878208e-24.
      This suggests that the observed relationship between maternal age and
      DNMs is due to a true effect of age and not on random chance.
      
Step 2.4

Use the paternal regression model to predict the expected number of paternal DNMs for a father of age 50.5.
    predicted_DNMs <- predict(paternal_lm, newdata = tibble(Father_age = 50.5))
    print(predicted_DNMs)
    output: ~78.7
    
Step 2.6

1. What is the “size” of this relationship (i.e., the average difference in counts of maternal and paternal DNMs)?
    Interpret the difference in plain language.
      Does it match your plot?
        The average difference is -39.23485, meaning that there are ~39 fewer DNMs in
        the maternal group than paternal. It does match the plot because the paternal
        data is generally higher than the maternal.

2. Is the relationship significant?
    How do you know? Explain the p-value in plain but precise language.
      The relationship is very significant because the p-value is <0.01 (it is 
      <2e-16 ***). This indicates that the average difference in DNMs observed
      between the maternal and paternal data is truly due to a difference in the
      groups and not random chance.
      
3. The coefficient estimate for the intercept term also gives
   the average difference per proband between maternal and paternal DNM counts.

Exercise 3

3.1
Data set chosen:
National Science Foundation Grant Terminations under the Trump Administration

3.2
You can see from the bar graph relating number of grants terminated to state
that California had the highest number of terminations, raising the question of
whether this observation is due simply to California's size or being targeted for its
liberal policies.

3.3
Hypothesis: some directorates will exhibit higher significantly obligated spending amounts
versus others.

Results: The "Technology, Innovation and Partnerships" directorate has higher obligated amounts
relative to other directorates with a value of 0.580312.

          The R-squared value is ~0.24, suggesting modest explanatory power.
