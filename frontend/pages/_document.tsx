import { Html, Head, Main, NextScript } from "next/document";

export default function Document() {
  return (
    <Html lang="en">
      <Head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="description" content="FlavorSnap - AI-powered Nigerian food recognition and recipe discovery" />
      </Head>
      <body className="antialiased">
        <div id="skip-to-content">
          <a href="#main-content" className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 bg-blue-600 text-white px-4 py-2 rounded-md z-50">
            Skip to main content
          </a>
        </div>
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
