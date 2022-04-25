from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BUTTONS = {
    "generate_code": InlineKeyboardMarkup([
        [InlineKeyboardButton(text="generate code", callback_data="Generate")]]),  # Create a Inline Button For Generate TD Code
    "submit_answers": InlineKeyboardMarkup([
        [InlineKeyboardButton(text="submit ✅", callback_data="submit"), InlineKeyboardButton(text="cancel ❌", callback_data="cancel")]])  # Create a Inline Button For Submit or Cancel The User Answers
}  # Inline Button Data`s

MESSAGES = {
    "start": """
    Welcome to the TD code making robot 🤖

Send /help command to receive help and document
 
to Generate the TD code, send the /generate command or use the «generate code» button""",  # message text when user send /start command
    "help": """
    A robot to build TD code 🤖

Send the /generate code command or use the «generate code» button to generate the TD code

The submitted data should be in the following order:


«country_code»🏳️:  3 letters code(ESP) or country name(Spain),

«document_number»📃:  Document number(ID9875401),

«birth_date»🎊:  Birth Of Date in Format " YYMMDD"(820512),

«sex»⚧:  Genre. Male or Female or Undefined,

«expiry_date»❌: The Expire Date in Format  "YYMMDD"(190622),

«nationality»🌍:  3 letters code(ESP) or country name(Spain),

«surname»👤:  Holder primary identifier(ESPAÑOLA ESPAÑOLA),

«given_names»👥:  Holder secondary identifier(CARMEN),

«optional_data»✅:  Optional personal data at the discretion of the issuing State(99999999R) Non-mandatory field. Empty string by default""",  # message text when user send /help command
    "cancel": """🤖 Generate TD1 Code Canceled

For Generate New TD1 Code Send /generate Command Or Use The «generate code» button""",  # message text when user cancel answers
}  # Message Text`s For Send to The User

QUESTIONS = [
    {
        "count": 0,
        "text": """1️⃣ - Enter The country_code:

ℹ️ - 3 letters code example: ESP | or country name example: Spain""",
        "button": None
    },
    {
        "count": 1,
        "text": """2️⃣ - Enter The document_number:

ℹ️ - example: ID9875401""",
        "button": None
    },
    {
        "count": 2,
        "text": """3️⃣ - Enter The birth_date:

ℹ️ - in Format YYMMDD example: 820512""",
        "button": None
    },
    {
        "count": 3,
        "text": """4️⃣ - Select The sex:

ℹ️ - Male or Female or Undefined""",
        "button": InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Male", "M"),
                InlineKeyboardButton("Female", "F"),
            ],
            [
                InlineKeyboardButton("Undefined", "X"),
            ]
        ])
    },
    {
        "count": 4,
        "text": """5️⃣ - Enter The expiry_date:

ℹ️ - in Format YYMMDD example: 190622""",
        "button": None
    },
    {
        "count": 5,
        "text": """6️⃣ - Enter The nationality:

ℹ️ - 3 letters code example: ESP | or country name example: Spain""",
        "button": None
    },
    {
        "count": 6,
        "text": """7️⃣ - Enter The surname:

ℹ️ - example: ESPAÑOLA ESPAÑOLA""",
        "button": None
    },
    {
        "count": 7,
        "text": """8️⃣ - Enter The given_names:

ℹ️ - example: CARMEN""",
        "button": None
    },
    {
        "count": 8,
        "text": """9️⃣ - Enter The optional_data:

ℹ️ - example: 99999999R
ℹ️ - can select ignore button""",
        "button": InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Ignore", callback_data="Ignore")]
        ])
    },
]  # Question Text`s And Button`s

ERRORS = {
    "invalid_country_name": """❌ invalid Value ❌

ℹ️ - 3 letters code example: ESP | or country name example: Spain""",  # when User Send Invalid Country And Nationality Name
    "invalid_date_format": """❌ invalid Date Format ❌

ℹ️ - in Format YYMMDD example: 820512""",  # when User Send Invalid Date
    "select_button": """❌ Invalid message, please Select Button ❌""",  # when User Can Only Select Inline Buttons
    "invalid_message": """❌ Invalid Message ❌
For Generate TD Code, Send /generate Command or Select «generate code» Button""",  # when User Send Answer When dont send /generate Code, Or Expired The User key in Redis
}  # Error Messages
