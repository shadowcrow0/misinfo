md<-aov(MAD~sys,
         data=avg_measures.1a2)
summary(md)
             Df   Sum Sq Mean Sq F value Pr(>F)
sys           1     2157    2157   0.033  0.856
Residuals   242 15793797   65264               
10 observations deleted due to missingness
TukeyHSD(md)
  Tukey multiple comparisons of means
    95% family-wise confidence level

Fit: aov(formula = MAD ~ sys, data = avg_measures.1a2)

$sys
         diff       lwr      upr     p adj
2-1 -6.354184 -75.20363 62.49526 0.8558949
