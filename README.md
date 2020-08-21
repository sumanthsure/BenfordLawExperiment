# Benford Law Experiment
### What is Benford Law
Benford law(First Digit Law) states that in any naturally occurring collections of numbers,
the leading significant digit/MSD(Most Significant digit) is likely to be small.
If we assume that the digits were distributed uniformly. Sample space for MSD(1,2,..9) 9 digits, then each digit would have occurred about 11.1% (1/9) of the time.
But this doesn't happen in the real world! Benford law captures that anomalous distribution. Sorce[ wikipedia](https://en.wikipedia.org/wiki/Benford%27s_law)

As a case study taken from [Brilliant.org](https://brilliant.org/wiki/benfords-law/)

- Here is a table with percentages that capture the 196 countries Area.
The "BL prediction" column is the percentage that Benford's law predicts for each digit. 
the number 1 appears as the leading significant digit about 30% of the time, 
while 9 appears as the leading significant digit less than 5% of the time.
Benford's law also makes predictions about the distribution of second digits, 
third digits, digit combinations, and so on.

    |First digit|	Number of countries	|Percentage	|BL prediction|
    ------------- |------------- |------------- |-------------
    |1	|6	|29%|30%
    |2	|37	|19%|18%
    |3	|23 |12%|12%
    |4	|22	|11%|10%
    |5	|11	|6%	|8%
    |6	|16	|8%	|7%
    |7	|12 |6%	|6%
    |8	|8	|4%	|5%
    |9	|11	|6%	|4%

### How do I see It
The law works on the distribution of numbers if that distribution spans over multiple magnitudes.
Here I don't want to prove as it involves complex maths but as an engineer want to test how it works with images and how does it behave with different types of images.

### Experiment
- With an RGB colour image each pixel is made up of three numbers to represent the Red(0-255), Green(0-255) and Blue(0-255) values.
  The value of each color indicates the density of color in that pixel. An Image is made up of tons of pixel hence I will use Each Image and Verify whether the pixel values of that Image
  Fits with Benford's Law Prediction. So In order to Fit with Benford's law, the probability of MSD of Pixel Values of that image should more likely be 1 then 2 and so on decreasing till 9.
- Here in this experiment, I have collected 25 random images from google[]() which consists of some clear images and some blur images.

[Dataset](https://github.com/sumanthsure/BenfordLawExperiment/tree/master/dataset)

Used python [script](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/scriptAndoutput/Test.py) to extract pixel values from images and get the MSD of Each Number and store it in the dictionary(counting the occurrences) and sort it w.r.to to its Frequency.

### Do you want to Take a guess?
As I have 2 types of datasets one clear images and other blur images what do you think does Benford law follow for both types of images?

### Observations

The most interesting part of the experiment :-P

The results were quite stunning. Almost all the images(Clear/Blur images) had the most frequent digit as 1(MSD).
But Hold on Don't change your answers.

Few results captured here

**ClearImages Outputs:**

ImageName: [1.jpeg](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/dataset/1.jpeg)

`{1: 52140, 2: 21573, 3: 20542, 4: 13129, 5: 9440, 9: 9291, 8: 7867, 7: 7312, 6: 7137}`

ImageName: [4.jpeg](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/dataset/4.jpeg)

`{1: 8322809, 2: 5182842, 3: 1510828, 4: 1360005, 5: 1307336, 6: 1218815, 7: 1147098, 8: 972393, 9: 862835}`

ImageName: [6.jpeg](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/dataset/6.jpeg)

`{1: 412874, 2: 116324, 3: 63072, 4: 60124, 5: 59416, 6: 59202, 7: 58944, 8: 55835, 9: 53810}`

ImageName: [8.jpeg](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/dataset/8.jpeg)

`{2: 14269698, 1: 9971172, 4: 1916852, 3: 1822086, 7: 1711544, 5: 1669261, 6: 1648444, 8: 1489416, 9: 1252764}`

ImageName: [13.jpeg](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/dataset/13.jpeg)

`{1: 295099, 2: 202540, 3: 77190, 4: 54971, 5: 42505, 6: 38312, 7: 36387, 9: 29779, 8: 29732}`

ImageName: [14.jpeg](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/dataset/14.jpeg)

`{1: 51165, 5: 13770, 4: 13175, 6: 13022, 8: 12432, 7: 12275, 2: 11836, 9: 11208, 3: 9820}`

ImageName: [16.jpeg](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/dataset/16.jpeg)

`{2: 199207, 1: 128569, 3: 12458, 4: 10059, 5: 8965, 6: 8482, 7: 7304, 8: 6895, 9: 6564}`

ImageName: [19.jpeg](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/dataset/19.jpeg)

`{1: 104251, 2: 72248, 8: 12740, 6: 12308, 9: 10535, 7: 10200, 5: 8808, 3: 7604, 4: 6223}`

ImageName: [20.jpeg](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/dataset/20.jpeg)

`{1: 957314, 2: 627375, 3: 358111, 4: 357421, 5: 305845, 6: 230944, 7: 143891, 8: 115389, 9: 113790}`

**BlurImages Outputs:**

ImageName: [b_1.jpeg](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/dataset/b_1.jpeg)

`{2: 75680, 1: 39616, 9: 10051, 8: 7149, 3: 6850, 7: 4307, 4: 3024, 6: 2305, 5: 2095}`

ImageName: [b_3.jpg](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/dataset/b_3.jpg)

`{1: 1157347, 2: 329244, 5: 203509, 6: 190063, 8: 189189, 7: 188227, 9: 182061, 4: 176101, 3: 147946}`

ImageName: [b_l_5.jpg](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/dataset/b_l_5.jpg)

`{1: 1301842, 2: 548830, 9: 103763, 8: 100912, 7: 96906, 6: 85240, 5: 58263, 4: 36670, 3: 27239}`

[AllOutputs](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/scriptAndoutput/Results.txt)

Plotting the curve: Python has a custom [library](https://pypi.org/project/benfordslaw/) for Benford law. Used it to plot some curves.

Clear Image Benford law Plot: The plot approximately fits with the benford curve ![Clear Image](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/plots/FitBL.png "Clear Image BL Plot")


Blur Image Benford law Plot: The plot doesn't fit with the benford curve ![Blur Image](https://github.com/sumanthsure/BenfordLawExperiment/blob/master/plots/Doesn'tFitBL.png "Blur Image BL Plot")


Having a small dataset it is hard to come to conclusions. But we can draw some observations 
seeing the above results some clear images didn't fit into the Benford curve as expected but most of them did. But seeing the blur images results none of them have fit into Benford curve.

Indeed images also follow Benford law.

But I want to draw your attention towards the images 4.jpeg, 6.jpeg, 10.jpeg they exactly satisfies Benford law and Seeing those images they are stunning images(Distribution of colors in those 
images is remarkable).

Strange conclusion Does that mean Benford law Describes the images whether they are beautiful or not? If you have heard about the [Golden](https://www.ucsart.com/learn/blog/learn-the-golden-ratio-for-your-artworks-on-canvas) ratio(1.61803)
this ratio creates pleasing aesthetic paintings. [Fibonacci](http://www.eniscuola.net/en/2016/06/27/the-numbers-of-nature-the-fibonacci-sequence/) series defines many laws of nature.. In my opinion, numbers do well in defining things better than humans.
Benford law somehow indirectly deals with the distribution of colors across an image.

Quest To found Benfordness should never be stopped

In my further experiment will try to increase my Dataset and will include more observations.


## Acknowledgement
I have heard this law while watching a youtube video and which made me think and went to discuss it with my teammates in a meeting. Astonishingly one of my teammates Nandu verified
the law then and there itself by taking powers of 2[link](https://ideone.com/UguCgq) and my manager Vijay went to explore this as well. Quite surprisingly he did it in a very different way I would recommend readers to check
his blog how did he do [link](https://lvijay.wordpress.com/2020/08/18/awk/).. Thanks to my manager who created avidity inside me to explore.

>I feel Benford law resides everywhere Just you have to dig deep to find it..
