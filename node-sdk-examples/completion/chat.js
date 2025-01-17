const Writer = require('writer-sdk');
const dotenv = require('dotenv');

dotenv.config();

const client = new Writer({
    apiKey: process.env.WRITER_API_KEY,
});

async function main() {
    try {
      const chat = await client.chat.chat({
        messages: [
          {
              role: "user",
              content: "You are an expert at writing concise product descriptions for an E-Commerce Retailer"
          },
          {
              role: "assistant",
              content: "Okay, great I can help write these descriptions. Do you have a specific product in mind?"
          },
          {
              role: "user",
              content: "Please write a one sentence product description for a cozy, stylish sweater suitable for both casual and formal occasions"
          }
        ],
        model: 'palmyra-x-004',
      });
      console.log(chat.choices[0].message.content);
    } catch (error) {
      console.error('Error:', error);
    }
  }

main();