using AutoMapper_Example.Data;
using System;

namespace AutoMapper_Example
{
    class Program
    {
        static void Main(string[] args)
        {
            var mapper = new AutoMapperConfig();
            var user = new User
            {
                FirstName = "Imie",
                LastName = "Nazwisko",
                City = "Miasto",
                Adress = "Adres"
            };
            var dto = mapper.MapUserToUserDto(user);
            Console.WriteLine(dto.Name);
            Console.WriteLine(dto.LastName);
        }
    }
}
