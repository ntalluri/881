In this article, the authors built a convolutional neural network (CNN) that predicts whether a patient will develop nonmelanoma skin cancer (NMSC) within the next year. The data came from a sample of 2 million patients in Taiwan's National Health Insurance Research Database. The authors selected 1829 patients whose first cancer was NMSC and 7665 cancer-free patients as controls. Cases were confirmed by diagnosis codes, procedure codes, and catastrophic illness certificates. The model used 3 years of records to predict NMSC onset 1 year later.

Each patient's records were converted into an image-like matrix. The rows were diagnosis codes and drug codes, and the columns represented time. This structure preserved the sequence of visits and prescriptions. Age, sex, and encounter counts were also included as inputs.

The CNN applied convolutions along the time axis of these matrices, and the authors evaluated it with 5-fold cross-validation. They compared three input sets: diagnoses only, medications only, and both. They also assessed feature importance by removing features one at a time and measuring the drop in AUROC.

The model using both input sets had an AUROC of 0.894, compared with 0.820 for diagnoses only and 0.879 for medications only. Removing carcinoma in situ of skin lowered the AUROC the most (2.8%). Removing trazodone, acarbose, or degenerative osteopathy each lowered the AUROC by more than 2%. The authors noted that this analysis does not show whether a feature raises or lowers risk. They also acknowledged that the data lacked UV exposure, lifestyle, family history, and NMSC subtype.

When I started reading this article, I assumed the authors were using images of skin cancer. Learning that they used medical records instead was interesting to me. The part I found most interesting was the use of temporal data. I had not considered structuring data as a matrix with time as the horizontal axis.

I was curious whether the records contain clear indicators of skin cancer. If so, what would happen to the model's performance if those were removed? I know the authors assessed feature importance, but most features appeared to be groups (such as drug classes) rather than single items.

I agree that this model is limited to a single ethnic population. However, as the authors mention, the approach could be applied to similar data. My concern is that nationality would also matter when applying it to other populations. Health care systems and available medications differ across countries, so I would expect the results to vary.

Disscussion questions
1) What is the best way to deal with data leakage in this form of data?
2) The feature removal cannot show whether a feature raises or lowers risk. How could CNN models on medical records be made interpretable for clinicians?