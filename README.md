# openaiisrich

openai is rich -- pricing information of openai models as JSON, incl. prompt and completion costs (`n_context_tokens_total`, `n_generated_tokens_total`).

pull requests welcome to keep the information up-to-date.

automatically updated on PyPi at each commit.

## Usage

### Usage in Python

Install with `pip install openaiisrich`

Then

```python
import openaiisrich

print("cost ", openaiisrich.cost("gpt-4", 507, 2987))

```

### Usage in Javascript

TODO

## License

MIT
