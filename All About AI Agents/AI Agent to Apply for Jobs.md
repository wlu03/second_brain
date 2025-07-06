| Layer                              | What it does                                                                                                  | Key libs / APIs                                                                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Browser control**                | Navigate, read the DOM, type & click                                                                          | Playwright (Python)                                                                                                                |
| **Form introspection**             | Collect `label / placeholder / name / options` for every `<input>`, `<textarea>`, `<select>`                  | Tiny helper in Python                                                                                                              |
| **Reasoning / content generation** | Given (A) the extracted schema + (B) your candidate profile, output a **JSON answer sheet**                   | OpenAI Chat / Anthropic Claude with **function‑calling**                                                                           |
| **Filler**                         | Map JSON answers back to selectors and call `page.fill()` / `page.select_option()` / `page.set_input_files()` | Python glue code                                                                                                                   |
| **Orchestration (optional)**       | Expose the above as an **MCP tool** so higher‑level agents can chain it                                       | `@playwright/mcp`, LangChain, or OpenAI Operator​[Wikipedia](https://en.wikipedia.org/wiki/OpenAI_Operator?utm_source=chatgpt.com) |
- PDF to text tool: `pdf_parser.py`
- define a parse resume schema using LLM. ask to pull out the fields we care about.

```

main()
query = "I want to apply for jobs at FAANG companies"
resume = get_resume("resume.pdf")

// using queries, I want to go to database to get application link that match the user query
application_arr = get_links(query)

//apply to each application link in array 

for i in range(application_arr.length)
	page = application_arr[i]
	
	PROFILE = parse_resume(resume) //get text
	schema = extract_form_schema(job_page) //get schema for the job
	answer = call_llm(schema, PROFILE) // use LLM to fill in the answer to get a newly filled out schema
	smart_fill(job_page, answer)
	email_arr = find_recruiter_emails(schema.job_title)
	send_emails(email_arr)

find_recruiter_emails(job_title)
	// do a deep search for a recruiters email and use an llm to send a custom email
	// if there exists a "Exact Match"/"Best Match" no need to deep search for an email just use these
		// break and return email
		
	//return an arr of recruiter email
	// cache recruiters emails
	
send_email(email_arr)
	// given email list
	for i in range(email_arr):
		// llm call to make a string to send
		// send email to recruiter

extract_form_schema(job_page)
	// crawls through the website and gets a JSON of the website
	// return a JSON of fields

smart_fill(job_page, answer)
	// use LLM to find which application it belongs to
	// and send it to a specific worker

greenhouse_worker()
	...
workday_worker()
	...
custom_worker()
	...




```