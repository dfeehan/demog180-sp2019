test = {
  'name': 'q6',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(party_degree.where("party","Democrat").column('degree mean')[0],0)
          175.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(party_degree.where("party","Independent").column('degree mean')[0],3)
          145.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(party_degree.where("party","Republican").column('degree mean')[0],3)
          191.113
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
