# PRC Challenge using LLMs

This proof of concept aims to use LLMs to predict fuel burnt by planes instead of standard simulations, algorithms or models.

Because of their inside knowledge and reasoning capabilities, LLMs already know important data like plane consumption for a specific model in a specific phase. They can also detect and deal with noisy data well.

Additionally, because of the interpretable nature of language, they are able to reflect on their own performance in order to self improve. My first attempt used this concept and the [GEPA](https://arxiv.org/abs/2507.19457) algorithm to optimize the prompt of a fuel predictor (but I didn't have time to do it for this attempt).

Finally, LLM predictions are by nature interpretable, because you can expose their reasoning. See example below:

<img width="1437" height="866" alt="image" src="https://github.com/user-attachments/assets/7c4906b7-3bad-408b-aac9-1ff585d5bf1f" />

The main challenge was the huge amount of predictions to do (around 70k). I wouldn't care if I was rich, but I ended up spending most of my time trying to go from thousand of dollars worth of LLM calls to just around $10. For that, I:
1. Summarized the features of data points in text to reduce the amount of token per prediction
2. Implemented an [experimental Batch API support](https://github.com/stanfordnlp/dspy/issues/9102) for [DSPy](https://github.com/stanfordnlp/dspy).

This method is scalable with the amount of compute (money) you're willing to give it. I went as low as 180 in RMSE over 100 examples when using Ensemble method over the best performing models (like GPT-5.1).

## How to reproduce?

I would advise against it. In the end, this is more of a personal challenge than an actual viable solution. I didn't have time to clean the notebooks either. Finally, it costs money...

The standard pipeline consists in running the preprocessing (preprocess.ipynb) to create the features dataset, then creating and sending the batches to a Batch API endpoint (dspy_process.ipynb), with a little bit of retry loop in case of failure. The following function populates final_df with new predictions until there are no more empty rows:

```python
final_df, filled, remaining = await round_v2(
    fuel_cot,
    final_df,
    n_pred_per_batch=10_000,
    minimal_batch_threshold=200,
)
```
