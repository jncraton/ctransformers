from ctransformers import AutoModelForCausalLM


class TestModel:

    def test_generate(self, lib):
        llm = AutoModelForCausalLM.from_pretrained('marella/gpt-2-ggml',
                                                   lib=lib)
        response = llm('AI is going to', seed=5, max_new_tokens=3)
        assert response == ' be a big'