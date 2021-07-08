using AutoMapper;

namespace AutoMapper_Example.Data
{
    public class AutoMapperConfig
    {
        private IMapper _mapper;
        public AutoMapperConfig()
        {
            _mapper = new MapperConfiguration(cfg =>
            {
                //there will be mapper configuration
            }).CreateMapper();
        }
    }
}
