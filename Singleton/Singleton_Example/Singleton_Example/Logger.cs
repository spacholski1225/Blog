using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Singleton_Example
{
    public class Logger
    {
        static readonly Logger logger = new Logger();
        private Logger()
        {
            Console.WriteLine("logger called");
        }
        public static Logger getLogger()
        {
            return logger;
        }
    }
}
