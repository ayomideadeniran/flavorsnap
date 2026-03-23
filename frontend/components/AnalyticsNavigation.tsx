import React from 'react';
import { useRouter } from 'next/router';
import { Home, BarChart3, Camera, Settings } from 'lucide-react';

const AnalyticsNavigation: React.FC = () => {
  const router = useRouter();

  const navigationItems = [
    { icon: Home, label: 'Home', href: '/', description: 'Navigate to home page' },
    { icon: Camera, label: 'Classify', href: '/classify', description: 'Classify food dishes with AI' },
    { icon: BarChart3, label: 'Analytics', href: '/analytics', description: 'View analytics dashboard' },
    { icon: Settings, label: 'Settings', href: '/settings', description: 'Access application settings' }
  ];

  const handleKeyDown = (e: React.KeyboardEvent, href: string) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      router.push(href);
    }
  };

  return (
    <nav className="bg-white shadow-sm border-b border-gray-200" role="navigation" aria-label="Main navigation">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <h1 className="text-xl font-bold text-gray-900">🍲 FlavorSnap</h1>
          </div>
          <ul className="flex items-center space-x-4" role="menubar">
            {navigationItems.map((item) => (
              <li key={item.href} role="none">
                <button
                  onClick={() => router.push(item.href)}
                  onKeyDown={(e) => handleKeyDown(e, item.href)}
                  className={`flex items-center gap-2 px-3 py-2 rounded-md text-sm font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 ${
                    router.pathname === item.href
                      ? 'bg-blue-100 text-blue-700'
                      : 'text-gray-600 hover:text-gray-900 hover:bg-gray-100'
                  }`}
                  role="menuitem"
                  aria-current={router.pathname === item.href ? 'page' : undefined}
                  aria-describedby={`${item.label}-desc`}
                >
                  <item.icon className="w-4 h-4" aria-hidden="true" />
                  {item.label}
                </button>
                <span id={`${item.label}-desc`} className="sr-only">
                  {item.description}
                </span>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default AnalyticsNavigation;
