using AutoMapper_Example;
using AutoMapper_Example.Data;
using AutoMapper_Example.Dto;
using Moq;
using System;
using Xunit;

namespace AutoMapperTest
{
    public class AutoMapperTest
    {
        private readonly Mock<AutoMapperConfig> _mapper;
        public AutoMapperTest()
        {
            _mapper = new Mock<AutoMapperConfig>();
        }
        [Fact]
        public void UserDtoIsMappedToUserType()
        {
            //arrange
            var user = new User
            {
                FirstName = "Imie",
                LastName = "Nazwisko",
                City = "Miasto",
                Adress = "Adres"
            };
            //act
            var dto = _mapper.Object.MapUserToUserDto(user);
            //assert
            Assert.IsType<UserDto>(dto);
        }
    }
}
