test = {
  'name': 'q26',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sim_results_aggregate.column('num_infected_degree mean').mean()<sim_results_aggregate.column('num_infected_ec mean').mean()
          True
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
