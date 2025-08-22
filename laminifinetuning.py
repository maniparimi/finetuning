import lamini
from lamini import Lamini

lamini.api_key = "YOUR_API_KEY"
lm = Lamini(model_name="meta-llama/meta-llama-3-8b-instruct")
data = get_data()

lm.tune(data=data)

fine_tune_args = {
    "learning_rate": 1.4e-4
}
lm.tune(data=data, **fine_tune_args)

