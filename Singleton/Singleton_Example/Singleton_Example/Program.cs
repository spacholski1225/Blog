using System;
using System.Threading;

namespace Singleton_Example
{
    class Program
    {
        static void Main(string[] args)
        {
            new Thread(() =>
            {
                for (int i = 0; i < 100; i++)
                {
                    Logger.getLogger();
                }
            }).Start();
            new Thread(() =>
            {
                for (int i = 0; i < 100; i++)
                {
                    Logger.getLogger();
                }
            }).Start();
        }
    }
}
