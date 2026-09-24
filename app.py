from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mara River - The Heart of Maasai Mara</title>
<script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-[#f0f9ff]">

<header class="bg-blue-900 text-white px-6 py-4 flex justify-between">
  <h1 class="font-black text-xl">MARA RIVER SAFARIS</h1>
  <span class="bg-amber-400 text-black px-3 py-1 rounded-full text-xs font-bold">Trans Mara - Kenya / Tanzania</span>
</header>

<div class="bg-gradient-to-br from-blue-900 via-blue-700 to-teal-600 text-white text-center py-20 px-4">
  <h2 class="text-5xl font-black">MARA RIVER</h2>
  <p class="mt-3 text-2xl italic text-blue-200">"Where the Great Migration Crosses"</p>
  <p class="mt-2">World Famous River in Maasai Mara National Reserve - Lolgorien, Trans Mara South</p>
  <div class="mt-8 flex justify-center gap-4">
    <span class="bg-white/20 px-4 py-2 rounded-full">🐊 Crocodiles</span>
    <span class="bg-white/20 px-4 py-2 rounded-full">🦛 Hippos</span>
    <span class="bg-white/20 px-4 py-2 rounded-full">🦓 Wildebeest Migration</span>
  </div>
</div>

<section class="max-w-6xl mx-auto grid md:grid-cols-3 gap-6 -mt-10 px-6">
  <div class="bg-white p-6 rounded-2xl shadow-lg text-center border-b-4 border-blue-900">
    <h3 class="font-bold">The Great Migration</h3>
    <p class="text-sm text-gray-600 mt-2">Over 1.5 Million wildebeest cross Mara River every July-October</p>
  </div>
  <div class="bg-white p-6 rounded-2xl shadow-lg text-center border-b-4 border-amber-500">
    <h3 class="font-bold">Location</h3>
    <p class="text-sm text-gray-600 mt-2">From Mau Forest to Lake Victoria<br>395km Long</p>
  </div>
  <div class="bg-white p-6 rounded-2xl shadow-lg text-center border-b-4 border-green-600">
    <h3 class="font-bold">Activities</h3>
    <p class="text-sm text-gray-600 mt-2">Game Drives, River Safaris, Photography, Cultural Tours</p>
  </div>
</section>

<section class="max-w-6xl mx-auto p-8 mt-8 grid md:grid-cols-2 gap-8">
  <div>
    <h2 class="text-3xl font-bold text-blue-900">About Mara River</h2>
    <p class="mt-4 text-gray-700">
    Mara River is the lifeline of Maasai Mara and Serengeti ecosystem. It starts in Narok County, 
    passes near Lolgorien and Iltolish, and flows into Lake Victoria. Famous for dramatic wildebeest crossings 
    where crocodiles wait. The river supports hippos, elephants, and the Maasai community.
    </p>
    <ul class="mt-4 space-y-2">
      <li>✓ Best Time to Visit: July - October (Migration)</li>
      <li>✓ Nearest Town: Lolgorien (5km)</li>
      <li>✓ Park Entry: Via Talek, Sekenani, Oloololo Gates</li>
      <li>✓ Local Guides Available</li>
    </ul>
  </div>
  <div class="bg-blue-900 text-white p-6 rounded-2xl">
    <h3 class="font-bold text-xl">Book Your Tour</h3>
    <p class="mt-2 text-blue-200">Mara River Lodge | Camp | Day Trip from Lolgorien</p>
    <div class="mt-4 bg-white text-blue-900 p-4 rounded-xl">
      <p><b>Phone:</b> 07XX XXX XXX</p>
      <p><b>M-Pesa Till:</b> 123456</p>
      <p><b>Location:</b> Mara River Bridge, Lolgorien</p>
    </div>
    <a href="#" class="inline-block mt-4 bg-amber-400 text-black px-6 py-2 rounded-full font-bold">WhatsApp Booking</a>
  </div>
</section>

<footer class="bg-black text-white text-center p-6 mt-10">
  <p>© 2026 Mara River Safaris - Lolgorien, Trans Mara South</p>
  <p class="text-sm text-gray-400">Near Iltolish Mara Schools | PEFA Church Lolgorien Area</p>
</footer>

</body>
</html>
    """

if __name__ == '__main__':
    app.run(debug=True)
