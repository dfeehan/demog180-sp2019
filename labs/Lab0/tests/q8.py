test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type':'wwpp',
      'cases': [
        {
          
          'code': """
          >>> round(sd(make_array(2,4,6,8,10)),3) == 2.828
          True
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}