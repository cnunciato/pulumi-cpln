// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Cpln
{
    [CplnResourceType("cpln:index/secret:Secret")]
    public partial class Secret : global::Pulumi.CustomResource
    {
        [Output("aws")]
        public Output<Outputs.SecretAws?> Aws { get; private set; } = null!;

        [Output("azureConnector")]
        public Output<Outputs.SecretAzureConnector?> AzureConnector { get; private set; } = null!;

        [Output("azureSdk")]
        public Output<string?> AzureSdk { get; private set; } = null!;

        [Output("cplnId")]
        public Output<string> CplnId { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("dictionary")]
        public Output<ImmutableDictionary<string, string>?> Dictionary { get; private set; } = null!;

        [Output("dictionaryAsEnvs")]
        public Output<ImmutableDictionary<string, object>> DictionaryAsEnvs { get; private set; } = null!;

        [Output("docker")]
        public Output<string?> Docker { get; private set; } = null!;

        [Output("ecr")]
        public Output<Outputs.SecretEcr?> Ecr { get; private set; } = null!;

        [Output("gcp")]
        public Output<string?> Gcp { get; private set; } = null!;

        [Output("keypair")]
        public Output<Outputs.SecretKeypair?> Keypair { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("natsAccount")]
        public Output<Outputs.SecretNatsAccount?> NatsAccount { get; private set; } = null!;

        [Output("opaque")]
        public Output<Outputs.SecretOpaque?> Opaque { get; private set; } = null!;

        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;

        [Output("tls")]
        public Output<Outputs.SecretTls?> Tls { get; private set; } = null!;

        [Output("userpass")]
        public Output<Outputs.SecretUserpass?> Userpass { get; private set; } = null!;


        /// <summary>
        /// Create a Secret resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Secret(string name, SecretArgs? args = null, CustomResourceOptions? options = null)
            : base("cpln:index/secret:Secret", name, args ?? new SecretArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Secret(string name, Input<string> id, SecretState? state = null, CustomResourceOptions? options = null)
            : base("cpln:index/secret:Secret", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
                AdditionalSecretOutputs =
                {
                    "azureSdk",
                    "docker",
                    "gcp",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Secret resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Secret Get(string name, Input<string> id, SecretState? state = null, CustomResourceOptions? options = null)
        {
            return new Secret(name, id, state, options);
        }
    }

    public sealed class SecretArgs : global::Pulumi.ResourceArgs
    {
        [Input("aws")]
        public Input<Inputs.SecretAwsArgs>? Aws { get; set; }

        [Input("azureConnector")]
        public Input<Inputs.SecretAzureConnectorArgs>? AzureConnector { get; set; }

        [Input("azureSdk")]
        private Input<string>? _azureSdk;
        public Input<string>? AzureSdk
        {
            get => _azureSdk;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _azureSdk = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("dictionary")]
        private InputMap<string>? _dictionary;
        public InputMap<string> Dictionary
        {
            get => _dictionary ?? (_dictionary = new InputMap<string>());
            set => _dictionary = value;
        }

        [Input("docker")]
        private Input<string>? _docker;
        public Input<string>? Docker
        {
            get => _docker;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _docker = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("ecr")]
        public Input<Inputs.SecretEcrArgs>? Ecr { get; set; }

        [Input("gcp")]
        private Input<string>? _gcp;
        public Input<string>? Gcp
        {
            get => _gcp;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _gcp = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("keypair")]
        public Input<Inputs.SecretKeypairArgs>? Keypair { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("natsAccount")]
        public Input<Inputs.SecretNatsAccountArgs>? NatsAccount { get; set; }

        [Input("opaque")]
        public Input<Inputs.SecretOpaqueArgs>? Opaque { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        [Input("tls")]
        public Input<Inputs.SecretTlsArgs>? Tls { get; set; }

        [Input("userpass")]
        public Input<Inputs.SecretUserpassArgs>? Userpass { get; set; }

        public SecretArgs()
        {
        }
        public static new SecretArgs Empty => new SecretArgs();
    }

    public sealed class SecretState : global::Pulumi.ResourceArgs
    {
        [Input("aws")]
        public Input<Inputs.SecretAwsGetArgs>? Aws { get; set; }

        [Input("azureConnector")]
        public Input<Inputs.SecretAzureConnectorGetArgs>? AzureConnector { get; set; }

        [Input("azureSdk")]
        private Input<string>? _azureSdk;
        public Input<string>? AzureSdk
        {
            get => _azureSdk;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _azureSdk = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("cplnId")]
        public Input<string>? CplnId { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("dictionary")]
        private InputMap<string>? _dictionary;
        public InputMap<string> Dictionary
        {
            get => _dictionary ?? (_dictionary = new InputMap<string>());
            set => _dictionary = value;
        }

        [Input("dictionaryAsEnvs")]
        private InputMap<object>? _dictionaryAsEnvs;
        public InputMap<object> DictionaryAsEnvs
        {
            get => _dictionaryAsEnvs ?? (_dictionaryAsEnvs = new InputMap<object>());
            set => _dictionaryAsEnvs = value;
        }

        [Input("docker")]
        private Input<string>? _docker;
        public Input<string>? Docker
        {
            get => _docker;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _docker = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("ecr")]
        public Input<Inputs.SecretEcrGetArgs>? Ecr { get; set; }

        [Input("gcp")]
        private Input<string>? _gcp;
        public Input<string>? Gcp
        {
            get => _gcp;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _gcp = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("keypair")]
        public Input<Inputs.SecretKeypairGetArgs>? Keypair { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("natsAccount")]
        public Input<Inputs.SecretNatsAccountGetArgs>? NatsAccount { get; set; }

        [Input("opaque")]
        public Input<Inputs.SecretOpaqueGetArgs>? Opaque { get; set; }

        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        [Input("tls")]
        public Input<Inputs.SecretTlsGetArgs>? Tls { get; set; }

        [Input("userpass")]
        public Input<Inputs.SecretUserpassGetArgs>? Userpass { get; set; }

        public SecretState()
        {
        }
        public static new SecretState Empty => new SecretState();
    }
}