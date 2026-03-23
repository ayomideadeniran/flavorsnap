import { useRouter } from "next/router";
import Image from "next/image";
import hero from "@/public/images/hero_img.png";

export default function Home() {
  const router = useRouter();

  return (
    <div className="bg-muted min-h-screen flex flex-col items-center justify-center px-4 py-8">
      <header className="text-center max-w-2xl">
        <h1 className="text-4xl md:text-5xl font-bold text-primary mb-4">
          🍲 Flavorsnap
        </h1>
        <p className="text-gray-700 text-lg mb-6">
          Snap a picture of your food and let AI identify the dish and show you
          its recipe.
        </p>
        <nav className="flex gap-4 justify-center" aria-label="Main navigation">
          <button
            onClick={() => router.push("/classify")}
            className="bg-accent text-white px-6 py-3 rounded-full font-semibold hover:bg-orange-600 transition focus:outline-none focus:ring-4 focus:ring-orange-300 focus:ring-offset-2"
            aria-describedby="get-started-desc"
          >
            Get Started
          </button>
          <span id="get-started-desc" className="sr-only">
            Start classifying Nigerian food dishes with AI
          </span>
          <button
            onClick={() => router.push("/analytics")}
            className="bg-gray-700 text-white px-6 py-3 rounded-full font-semibold hover:bg-gray-800 transition focus:outline-none focus:ring-4 focus:ring-gray-400 focus:ring-offset-2"
            aria-describedby="analytics-desc"
          >
            View Analytics
          </button>
          <span id="analytics-desc" className="sr-only">
            View food classification analytics and usage statistics
          </span>
        </nav>
      </header>

      <main id="main-content" className="mt-10 w-full max-w-md">
        <Image
          src={hero}
          alt="Nigerian dish - Jollof rice served with plantains and vegetables"
          width={500}
          height={300}
          className="rounded-xl shadow-lg"
          priority
        />
      </main>

      <footer className="mt-12 text-gray-500 text-sm">
        <p>Built with 💚 for Nigerian food lovers</p>
      </footer>
    </div>
  );
}
