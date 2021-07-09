using AutoMapper;
using AutoMapper_Example.Dto;

namespace AutoMapper_Example.Data
{
    public class AutoMapperConfig
    {
        private IMapper _mapper;
        public AutoMapperConfig()
        {
            _mapper = new MapperConfiguration(cfg =>
            {
                cfg.CreateMap<User, UserDto>().ReverseMap();
            }).CreateMapper();
        }
        public UserDto MapUserToUserDto(User user)
        {
            return _mapper.Map<UserDto>(user);
        }
    }
}
