using AutoMapper_Example.Data;
using System;

namespace AutoMapper_Example
{
    class Program
    {
        static void Main(string[] args)
        {
            var user = new User
            {
                FirstName = "d",
                LastName = "s",
                City = "dd"
            };
            var mapper = new AutoMapperConfig();
            var dto = mapper.MapUserToUserDto(user);
            Console.WriteLine(dto.FirstName);
            Console.WriteLine(dto.LastName);
        }
    }
}
