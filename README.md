# MultiLyGAN
a new multi-classification machine learning pipeline MultiLyGAN to identity seven types of lysine modified sites 
![image](https://github.com/Lab-Xu/MultiLyGAN/blob/main/Figures/classification.png)
## Requirements
* Python>=3.7
* Matlab2016a
* Tensorflow =1.6.0

## File description
* In "Data" folder, we show the detailed information of seven types of lysine modified sites. 
* In "Data preprocessing" folder, we display the window cutting code and homologous sequences discarding code. 
* There are nine different encoding schemes in the folder named "Feature construction" which are AAindex, CKSAAP (Composition of K-space amino acid pairs), PWM (Position weight matrix), Reduced Alphabet, FoldAmyloid, BE (Binary Encoding), PC-PseAAC, SC-PseAAC, and Structure features. These programs can encode protein fragments into feature vectors of different dimensions.
* The folder named "Dimensionality reduction" is used to acquire effective features and remove redundant features.
* There are two sub-folders in the "sample augmentation" folder. To solve the data unbalanced issue, Conditional Generative Adversarial Network (CGAN) and Conditional Wasserstein Generative Adversarial Network (CWGAN), two influential deep generative methodology, were leveraged to generate synthetic samples.
* The folder named "Classification" is based on Random Forest (RF) to stratify seven classes.


The pipeline of identification of multiple protein modified sites is visualized. 

![image](https://github.com/Lab-Xu/MultiLyGAN/blob/main/Figures/workflow.png)
