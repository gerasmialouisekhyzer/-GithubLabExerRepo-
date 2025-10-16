[
  {
    $lookup: {
      from: "tracks",
      let: {
        albumId: "$AlbumId",
      },
      pipeline: [
        {
          $match: {
            $expr: {
              $eq: ["$AlbumId", "$$albumId"],
            },
          },
        },
        {
          $lookup: {
            from: "genres",
            localField: "GenreId",
            foreignField: "GenreId",
            as: "genre",
          },
        },
        {
          $unwind: {
            path: "$genre",
            preserveNullAndEmptyArrays: true,
          },
        },
        {
          $lookup: {
            from: "media_types",
            localField: "MediaTypeId",
            foreignField: "MediaTypeId",
            as: "media_type",
          },
        },
        {
          $unwind: {
            path: "$media_type",
            preserveNullAndEmptyArrays: true,
          },
        },
        {
          $lookup: {
            from: "playlist_track",
            localField: "TrackId",
            foreignField: "TrackId",
            as: "playlist_tracks",
          },
        },
        {
          $lookup: {
            from: "playlists",
            let: {
              plIds:
                "$playlist_tracks.PlaylistId",
            },
            pipeline: [
              {
                $match: {
                  $expr: {
                    $in: [
                      "$PlaylistId",
                      "$$plIds",
                    ],
                  },
                },
              },
            ],
            as: "playlists",
          },
        },
        {
          $lookup: {
            from: "invoice_items",
            localField: "TrackId",
            foreignField: "TrackId",
            as: "invoice_items",
          },
        },
        {
          $lookup: {
            from: "invoices",
            let: {
              invIds: "$invoice_items.InvoiceId",
            },
            pipeline: [
              {
                $match: {
                  $expr: {
                    $in: [
                      "$InvoiceId",
                      "$$invIds",
                    ],
                  },
                },
              },
              {
                $lookup: {
                  from: "customers",
                  localField: "CustomerId",
                  foreignField: "CustomerId",
                  as: "customer",
                },
              },
              {
                $unwind: {
                  path: "$customer",
                  preserveNullAndEmptyArrays: true,
                },
              },
              {
                $lookup: {
                  from: "employees",
                  let: {
                    repId:
                      "$customer.SupportRepId",
                  },
                  pipeline: [
                    {
                      $match: {
                        $expr: {
                          $eq: [
                            "$EmployeeId",
                            "$$repId",
                          ],
                        },
                      },
                    },
                  ],
                  as: "support_employee",
                },
              },
              {
                $unwind: {
                  path: "$support_employee",
                  preserveNullAndEmptyArrays: true,
                },
              },
              {
                $addFields: {
                  "customer.support_employee":
                    "$support_employee",
                },
              },
              {
                $project: {
                  support_employee: 0,
                },
              },
            ],
            as: "invoices",
          },
        },
      ],
      as: "tracks",
    },
  },
]