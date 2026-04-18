import re

filepath = r'C:/Users/suman/Reachr Linkedin/posts/raw-data/vaibhav-sisinty-linkedin-formatted.txt'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Map of unique URL fragment -> description to insert AFTER that IMAGE_N_URL line
descriptions = {
    # POST 3 - tweet screenshot
    'D5622AQEzIUEx1cg-pQ': (
        'IMAGE_1_DESCRIPTION: Screenshot of Vaibhav\'s own X/Twitter tweet: "The unit cost of intelligence is '
        'dropping at a pace that\'s unprecedented. The world needs a new way to value human intelligence very soon, '
        'Or we are soon cooked AF!" (39 likes, 8 replies). Pattern: sharing own tweet screenshot as the primary '
        'content of the LinkedIn post — cross-platform amplification of an idea.'
    ),
    # POST 4 - NVIDIA press release
    'D5610AQGuLnbr9H17rw': (
        'IMAGE_1_DESCRIPTION: NVIDIA official press release screenshot: "NVIDIA Launches Ising, the World\'s First '
        'Open AI Models to Accelerate the Path to Useful Quantum Computers" — dated April 14, 2026, with stylized '
        'quantum sphere visual. Pattern: primary source screenshot used to validate specific technical claims in a '
        'long-form breakdown post.'
    ),
    # POST 6 - promotional thumbnail
    'D5610AQHjEJkguYh5-g': (
        'IMAGE_1_DESCRIPTION: Podcast/promo thumbnail — a man in glasses and blue t-shirt, surrounded by asterisk '
        'star symbols (resembling Anthropic/voice-tech branding), with a Shure microphone and food imagery below. '
        'Appears to be a video thumbnail or sponsored promotional image. Pattern: attention-grabbing visual thumbnail '
        'attached to long-form Anthropic security analysis post to drive clicks.'
    ),
    # POST 7 - VCCiRCLE article
    'D5622AQGXx2XagH2nbA': (
        'IMAGE_1_DESCRIPTION: VCCiRCLE news article screenshot: "Consumer AI Startup Primetrace (Parent Of Kutumb) '
        'Hits Rs 200 Cr EBITDA Run Rate" — showing 4 Primetrace founders in matching black uniforms, with bullet '
        'points: Rs 550 Cr ARR with 50x growth in 3 years, 350 million cumulative downloads. Pattern: third-party '
        'news source screenshot to validate data claims about an Indian AI company success story.'
    ),
    # POST 12 - Raj Shamani podcast thumbnail
    'D5622AQG45goXRDpegg': (
        'IMAGE_1_DESCRIPTION: YouTube thumbnail for Raj Shamani podcast episode "AI Masterclass: Become an Expert '
        'at Claude, Gemini & Powerful AI Tools | Vaibhav | FO480 Raj Shamani" — split image of Raj Shamani (left, '
        'thinking pose, black t-shirt) and Vaibhav Sisinty (right, white sweater, speaking at Focusrite mic). '
        'Pattern: borrowed audience strategy — posting podcast appearance thumbnail to tap Raj Shamani\'s massive '
        'Indian LinkedIn/YouTube audience.'
    ),
    # POST 13 - Growth School photo
    'D5622AQFeyaMyzwPLYA': (
        'IMAGE_1_DESCRIPTION: Photo of Vaibhav Sisinty (right, black full-sleeve) with another man (left, white '
        'shirt) seated on a blue couch in front of the Growth School office logo (green arrow on wood paneling). '
        'Pattern: social proof / access photo showing connection to prominent Indian startup education space. '
        'Attached to post promoting Wispr voice dictation app.'
    ),
    # POST 18 - Peak XV Founder Retreat
    'D5622AQEwalOUNSNq1g': (
        'IMAGE_1_DESCRIPTION: Solo photo of Vaibhav Sisinty smiling in a black hoodie, standing in front of '
        '"peak xv | FOUNDER RETREAT - together for the climb" backdrop with Himalayan mountain image. Pattern: '
        'event access photo proving attendance at prestigious Peak XV (formerly Sequoia Capital India) founder '
        'retreat — establishes credibility alongside post praising Peak XV\'s $1.3B fundraise.'
    ),
    # POST 20 - IBM stock chart
    'D5622AQEpCszUnZSVJQ': (
        'IMAGE_1_DESCRIPTION: IBM Common Stock (NYSE: IBM) live stock chart showing sharp intraday decline: '
        '224.24 USD, -32.92 (-12.80%) on Feb 23, 3:35 PM EST. Previous close: 257.16. Chart shows steep cliff '
        'drop around 2 PM. Pattern: financial data screenshot as visual proof of the "IBM lost $31 billion '
        'overnight because Claude launched" headline — makes the abstract number viscerally real.'
    ),
    # POST 22 - tweet screenshot (highest comments post: 657 likes, 117 comments)
    'D5622AQFEWfM9XHXYWQ': (
        'IMAGE_1_DESCRIPTION: Screenshot of Vaibhav\'s own X/Twitter tweet: "At the speed AI is moving, It might '
        'be our last invention. Or our last mistake." — dark background, clean typography, @VaibhavSisinty with '
        'blue checkmark. Pattern: short punchy tweet screenshot as visual anchor for existential AI post. '
        'HIGHEST ENGAGEMENT post in dataset: 657 likes, 117 comments — proves this tweet-screenshot + '
        'existential AI hook format drives maximum comment engagement.'
    ),
    # POST 25 - Voice of India bar chart
    'D5622AQEKWL3a3hqDoQ': (
        'IMAGE_1_DESCRIPTION: "Voice of India" benchmark bar chart — "Accuracy Performance Across Speech '
        'Recognition Models: Average Accuracy (%) across 15 Indian Languages." Rankings from top: Sarvam Audio '
        '86.09%, Sarvam Saarika 84.12%, Google Gemini 3 Pro 83.6%, AI4Bharat IndicConformer 83.28%, Amazon '
        'Transcribe 78.05%, Microsoft STT 66.93%, Meta omniASR models 59-64%, OpenAI GPT-4o 35%, Assembly AI '
        '24.35% (bottom). Branded "Voice of India - The national measurement layer for voice AI in India." '
        'Pattern: proprietary research data visualization proving contrarian claim (Indian Sarvam beats global '
        'giants including OpenAI/Microsoft for Indian languages).'
    ),
    # POST 33 - Alexandr Wang meetup
    'D5622AQGKOgODtpFDqg': (
        'IMAGE_1_DESCRIPTION: Photo of Vaibhav Sisinty (right, brown sweater, white pants, smiling) with '
        'Alexandr Wang (left, glasses, black graphic t-shirt) in a restaurant with decorative plates on wall. '
        'Alexandr Wang = founder of Scale AI ($29B company), then VP of AI at Meta, leading superintelligence '
        'for 1B+ users. Pattern: high-status access post — meeting a top global AI figure. 1,286 likes, '
        '48 comments.'
    ),
    # POST 36 image 1 - Travis Kalanick selfie
    'D5622AQGLa7L1wiSAcQ': (
        'IMAGE_1_DESCRIPTION: Blurry selfie of Vaibhav Sisinty (left) with Travis Kalanick, Uber co-founder '
        '(right, dark curly hair, black shirt), at a party/event venue with purple/blue lighting. From the '
        'Uber Vegas celebration party when Vaibhav was 21 and Travis personally walked over and shook his hand. '
        'Pattern: nostalgia photo with famous founder establishing authentic personal connection to comeback story.'
    ),
    # POST 36 image 2 - ATOMS blog screenshot
    'D5622AQHSj4stA7hR2w': (
        'IMAGE_2_DESCRIPTION: Screenshot of Travis Kalanick\'s ATOMS website (dark background) — blog post '
        '"I\'m Back." by Travis Kalanick. Excerpt: "I often get the question from entrepreneurs or executives, '
        '\'What should I do next?\' My answer has always been \'become deeply self aware... The thing is, I '
        'never left.\'" Signed with Travis Kalanick\'s signature. ATOMS navigation shows Vision and Contact. '
        'Pattern: screenshot of referenced source to provide direct evidence for the Travis comeback narrative.'
    ),
    # POST 37 - AI research radar chart
    'D5622AQEQfF_l10VAIA': (
        'IMAGE_1_DESCRIPTION: Academic radar/spider chart titled "Theoretical capability and observed usage by '
        'occupational category" (Figure 2 from Anthropic research report). Large blue area = theoretical AI '
        'coverage across all job categories. Tiny red/pink area = actual observed AI usage. The gap is enormous. '
        'Categories: Management, Business & finance, Computer & math, Legal, Healthcare, Arts & media, Office & '
        'admin, Sales, Agriculture, Construction, etc. Caption: "Share of job tasks LLMs could theoretically '
        'perform vs. actual usage data." Pattern: Anthropic\'s own published research used to prove the '
        '"AI capability vs adoption gap" thesis — using the company\'s data against standard AI hype narrative.'
    ),
    # POST 48 image 1 - Josh Woodward formal portrait
    'D5622AQEq7T27xopJNg': (
        'IMAGE_1_DESCRIPTION: Professional portrait of Josh Woodward (left, red/auburn hair, glasses, gray polo '
        'shirt) and Vaibhav Sisinty (right, black zip-up sweater), posing together in a warm wood-paneled setting '
        'with plant in background. Josh Woodward = VP/Director at Google Labs, responsible for Gemini, NotebookLM, '
        'Google AI Studio, Pomelli, Stitch, Genie. Professional photography quality. Pattern: formal access photo '
        'establishing meeting with top-tier Google AI executive.'
    ),
    # POST 48 image 2 - candid meeting
    'D5622AQHGvYsAW6dw3g': (
        'IMAGE_2_DESCRIPTION: Candid dimly lit photo — Josh Woodward (blurred, back to camera, gesturing) and '
        'Vaibhav Sisinty (right, laughing, black outfit) at a round table with two MacBook laptops. Intimate '
        'working session atmosphere. Pattern: BTS candid showing actual intellectual exchange, not just a '
        'posed handshake — humanizes the meeting and signals depth of conversation.'
    ),
    # POST 48 image 3 - group corridor
    'D5622AQE3KfqS2VZLMA': (
        'IMAGE_3_DESCRIPTION: Photo in warmly lit corridor with wood paneling — Josh Woodward (left, black '
        't-shirt), another attendee with conference lanyard in center (graphic t-shirt, smiling), third person '
        'partially visible right. Candid networking moment. Pattern: shows multiple interactions at the same '
        'event — establishes Vaibhav as a genuine insider at this level, not a one-off encounter.'
    ),
    # POST 48 image 4 - formal seated conversation
    'D5622AQHeK6tbefhvUw': (
        'IMAGE_4_DESCRIPTION: Professional editorial photo — Josh Woodward (left) and Vaibhav Sisinty (right) '
        'seated across from each other at round table with two MacBooks between them, both gesturing actively '
        'mid-conversation. Both wearing Nike Jordan sneakers. Warm wood-paneled background. High-quality '
        'professional/editorial photography. Pattern: the "money shot" of the 4-image series — two people as '
        'equals in deep conversation, not a fan selfie. This 4-image series + Google exec = highest engagement '
        'post in dataset: 1,425 likes, 97 comments.'
    ),
}

# Replace each IMAGE_N_URL line by appending description after it
matched = 0
for url_fragment, description in descriptions.items():
    pattern = r'(IMAGE_\d+_URL: [^\n]*' + re.escape(url_fragment) + r'[^\n]*)'
    replacement = r'\1\n' + description
    new_content = re.sub(pattern, replacement, content)
    if new_content == content:
        print(f'WARNING: No match for {url_fragment[:30]}')
    else:
        content = new_content
        matched += 1
        print(f'OK [{matched}]: {url_fragment[:30]}')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nDone! {matched}/{len(descriptions)} descriptions added.')
