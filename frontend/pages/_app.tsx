import "@/styles/globals.css";
import type { AppProps } from "next/app";
import { useEffect } from "react";

export default function App({ Component, pageProps }: AppProps) {
  useEffect(() => {
    // Announce page changes to screen readers
    const handleRouteChange = () => {
      const announcement = document.getElementById('page-announcement');
      if (announcement) {
        announcement.textContent = document.title;
      }
    };

    // Initial announcement
    handleRouteChange();
  }, []);

  return (
    <>
      <div
        id="page-announcement"
        role="status"
        aria-live="polite"
        className="sr-only"
      />
      <Component {...pageProps} />
    </>
  );
}
